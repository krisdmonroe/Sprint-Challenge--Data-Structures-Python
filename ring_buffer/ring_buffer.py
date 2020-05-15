from reverse import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = LinkedList()

    def append(self, item):
        self.storage.add_to_end(item)
        self.size += 1
    def get(self):
        pass