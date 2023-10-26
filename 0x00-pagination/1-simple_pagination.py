#!/usr/bin/env python3
'''
Module Implement get_page to get paginated page
'''
import csv
import math
from typing import List, Tuple


class Server:
    """Server class implements methods
        dataset -> returns dataset to be paginated
        index_range -> calculate the start and end index for pagination
        get_page -> get a page from dataset given parameters
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Get page based on start index and end index
        Args:
            page:startIndex of page in dataset
            page_size: page_size index
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if page > len(self.dataset()) | page_size > len(self.dataset()):
            return []
        results = self.index_range(page, page_size)
        return self.dataset()[results[0]: results[1]]
