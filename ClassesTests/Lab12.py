class OpenAddressingHashMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
            self.p = 0

    def __init__(self):
        self.noneItem = OpenAddressingHashMap.Item(None)
        self.list = [self.noneItem, self.noneItem, self.noneItem, self.noneItem, self.noneItem]
        self.n = len(self.list)
        # self.num_items = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return is_empty(self.list)

    def probe(self, item):
        while self.list[item.key + item.p] is not None:
            item.p += 1

    def get_items(self):
        num_items = 0
        for i in range(len(self)):
            if self[i] is not None:
                num_items = +1
        return num_items

    def __getitem__(self, k):
        return self.list[k % self.n + ]

    def __setitem__(self, k, v):
