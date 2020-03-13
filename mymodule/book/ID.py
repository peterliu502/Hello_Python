#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def book_id(book):
    def ord2str(mychr):
        return str(ord(mychr))
    return ''.join(list(map(ord2str, [mychr for mychr in book])))

