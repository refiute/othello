#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 0: white
 1: black
-1: empty
"""
import subprocess
import numpy as np

d = [-1, 0, 1]
def is_in(mp, y, x):
    return 0 <= y < len(mp) and 0 <= x < len(mp[y])

def can_move(mp, y, x, color):
    place = []

    for i in range(0, 3):
        for j in range(0, 3):
            if i == 1 and j == 1:
                continue
            ny = y
            nx = x
            count = 0

            while True:
                ny += d[i]
                nx += d[j]

                if not is_in(mp, ny, nx) or mp[ny][nx] != (color^(1)):
                    break

                count += 1

            if not is_in(mp, ny, nx) or mp[ny][nx] != color or count == 0:
                continue

            place.append((d[i], d[j]))

    return place


def can_turn(mp, color):
    place = []
    for y in range(0, len(mp)):
        for x in range(0, len(mp[y])):
            if mp[y][x] == -1 and len(can_move(mp, y, x, color)) > 0:
                place.append((y, x))

    return place


def put_hand(mp, y, x, color):
    place = can_move(mp, y, x, color)
    if len(place) == 0:
        return Null

    for dy, dx in place:
        nx = x
        ny = y

        mp[ny][nx] = color

        while True:
            nx += dx
            ny += dy

            if mp[ny][nx] != (color^(1)):
                break

            mp[ny][nx] = color

    return mp

def count_empty(mp):
    count = 0
    for y in mp:
        for x in y:
            count += int(x == -1)
    return count

def init_mp():
    mp = np.zeros((8, 8), dtype=int)
    for y in range(0, len(mp)):
        for x in range(0, len(mp[y])):
            mp[y][x] = -1

    for y in [3, 4]:
        for x in [3, 4]:
            mp[y][x] = int(y!=x)

    return mp

def read_mp(filename):
    mp = []
    with open(filename) as f:
        for y in f.readlines():
            mp.append([int(x) for x in y.split()])

    return mp

def print_mp(mp):
    black = 0
    for y in mp:
        s = ""
        for x in y:
            black += int(s==1)
            s += u"●" if x == 0 else u"○" if x == 1 else "＿"
        print(s)
        print("black: %d, white %d"%(black, 64-black))

def run_program(program, mp, color):
    data = ""
    for x in mp:
        data += " ".join([str(y) for y in x])+"\n"

    data += str(color)+"\n"

    proc = subprocess.Popen(program, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newline=True)
    try:
        out, err = proc.communicate(input=data, timeout=5)
    except: TimeoutExpired:
        proc.kill()

    return out

if __name__ == "__main__":
    run_program("", init_mp(), "white")
