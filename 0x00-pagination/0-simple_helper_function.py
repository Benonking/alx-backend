#!/usr/bin/env python3

'''
simple helper function to a tuple, containg parameters

'''


def index_range(page, page_size):
    if page <= 0 or page_size <= 0:
        return None

    startIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (startIndex, endIndex)
