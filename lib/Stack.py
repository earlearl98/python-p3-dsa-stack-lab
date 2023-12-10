class Stack:
    def __init__(self, items=None, limit=100):
        self.items = [] if items is None else items
        self.limit = limit

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i
        return -1
