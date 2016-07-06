#!/usr/bin/env python
# coding: utf-8

import os
import sys
import argparse
import logging
import json

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.options

import othello

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        self.programs = kwargs.pop('programs')
        self.mp = kwargs.pop('mp')
        self.color = 0
        super(WSHandler, self).__init__(*args, **kwargs)

    def check_origin(self, origin):
        return True

    def open(self):
        print('connection opened ...')

    def on_close(self):
        print('connection closed ...')

    def on_message(self, message):
        # empty count
        empty = othello.count_empty(self.mp)
        if empty == 0:
            msg = json.dumps({"cmd": "end"})
            self.write_message(msg)
            self.close()
            return

        # pass check
        place = othello.can_turn(self.mp, self.color)
        if len(place) == 0:
            msg = json.dumps({"cmd": "pass", "color": self.color})
            self.write_message(msg)
            self.color ^= 1
            return

        out = othello.run_program(self.programs[self.color], self.mp, self.color)
        pos = tuple(map(int, out.split()))
        print(pos)

        # validate
        if not pos in place:
            msg = json.dumps({"cmd": "invalid", "color": self.color})
            print(msg)
            self.write_message(msg)
            self.close()
            return

        othello.put_hand(self.mp, pos[0], pos[1], self.color)

        msg = json.dumps({"cmd": "hand", "color": self.color, "mp": self.mp.tolist()})
        self.write_message(msg)

        othello.print_mp(self.mp)
        self.color ^= 1

def get_args():
    parser = argparse.ArgumentParser(description="othello server")
    parser.add_argument('program1', metavar="path_to_program1", type=str, help="user1's program")
    parser.add_argument('program2', metavar="path_to_program2", type=str, help="user2's program")
    parser.add_argument('--map', type=str, help="default map")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = get_args()

    if args.map:
        mp = othello.read_mp(args.map)
    else:
        mp = othello.init_mp()

    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r'/', MainHandler),
        (r'/ws', WSHandler, {'programs': [args.program1, args.program2], 'mp': mp}),
        (r'/assets/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), "assets")}),
    ], debug=True)
    application.listen(1919)

    tornado.ioloop.IOLoop.instance().start()
