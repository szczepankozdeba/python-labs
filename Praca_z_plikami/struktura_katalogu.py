#!/usr/bin/python3

import os

def list(directory, step):
    parts = os.listdir(directory)
    for part in parts:
        path = os.path.join(directory, part)
        print(step * "   " + part)
        if os.path.isdir(path):
            list(path, step + 1)

list(os.path.dirname(os.path.realpath(__file__)), 0)
