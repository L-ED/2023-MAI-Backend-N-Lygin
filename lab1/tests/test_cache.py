from typing import Any
from  backend.cache.lru_cache import LRUCache
import unittest

class Test_LRUCache(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = LRUCache(100)
        self.cache.set('Jesse', 'Pinkman')
        self.cache.set('Walter', 'White')
        self.cache.set('Jesse', 'James')

    def test_getter1(self):
        self.assertEqual(self.cache.get('Jesse'), 'James')
        self.cache.rem('Walter')
        self.assertEqual(self.cache.get('Walter'), '')