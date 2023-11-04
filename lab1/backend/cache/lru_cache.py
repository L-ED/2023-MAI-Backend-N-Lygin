from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        try:
            return self.cache[key]
        except KeyError as e:
            return ""#None

    def set(self, key: str, value: str) -> None:
        if len(self.cache)==self.capacity:
            self.cache.popitem(0)
        self.cache[key] = value

    def rem(self, key: str) -> None:
        del self.cache[key]