#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
'This is a minus module'

__author__ = 'Peterliu'


def myadd(*args):
    def add_2elm(elm1, elm2):
        return elm1 + elm2
    return functools.reduce(add_2elm, args)

