#!/usr/bin/env python
# coding: utf-8

import sys
import argparse

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

import othello

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, programs, mp):
        self.programs = programs
        self.mp = mp
        self.color = 0

    def open(self):
        print('connection opened ...')

    def on_close(self):
        print('connection closed ...')

    def on_message(self, message):
        # empty count
        empty = othello.count_empty(self.mp)
        if empty == 0:
            self.write_message({"cmd": "end"})
            self.close()
            return

        # pass check
        place = othello.can_turn(self.mp, self.color)
        if len(place) == 0:
            self.write_message({"cmd": "pass", "color": color})
            return
        
        out = othello.run_program(self.programs[color], self.mp, self.color)
        pos = tuple(out.split(", "))
        
        # validate
        if not out in place:
            self.write_message({"cmd": "invalid", "color": self.color})
            self.close()
            return
        
        othello.put_hand(self.mp, out[0], out[1], self.color)
        self.write_message({"cmd": "hand", "color": self.color, "map": self.mp})
        
        print(pos)
        othello.print_mp(self.mp)

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

    application = tornado.web.Application([
        (r'/', MainHandler),
        (r'/ws', WSHandler([args.program1, args.program2], mp))
    ])
    application.listen(1919)

    tornado.ioloop.IOLoop.instance().start()
