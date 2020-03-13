#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def student(*name):
    return {i: j for i, j in zip(range(len(name)), name)}

