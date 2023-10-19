#!/usr/bin/env python3

'''
simple helper function to return a tuple

'''


def index_range(page, page_size):
    '''
    caltulate startIndex and endIndex of page
    Args:
        page: file size
        page_size: pagnated page size
    '''
    if page <= 0 or page_size <= 0:
        return None

    startIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (startIndex, endIndex)
