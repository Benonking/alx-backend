import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if page > len(self.dataset()) | page_size > len(self.dataset()):
            return []
        results = self.index_range(page, page_size)
        return self.dataset()[results[0]: results[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        results = {}
        if (self.index_range(page, page_size)[1] < len(self.dataset())):
            results['prev_page'] = page + 1
        if (self.index_range(page, page_size)[0] > 0):
            results.next_page: page + 1
        results['totol_pages'] = len(self.dataset())
        results['data'] = self.get_page(page, page_size)
        results['page'] = page
        results['page_size'] = page_size
        return results
