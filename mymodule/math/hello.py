#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This is a hello module'

__author__ = 'Peterliu'

import sys


def hello():
    args = sys.argv
    if len(args) == 1:
        print('hello,world!')
    elif len(args) == 2:
        print('hello,{:s}'.format(args[1]))
    else:
        print('Too much arguements!')
    return


if __name__ == '__main__':
    hello()
