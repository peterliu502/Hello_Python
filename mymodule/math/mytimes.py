#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This is a add module'

__author__ = 'Peterliu'

import functools


def mytimes(*args):
    def times_2elm(elm1, elm2):
        return elm1 * elm2
    return functools.reduce(times_2elm, args)

