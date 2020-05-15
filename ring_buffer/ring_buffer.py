from reverse import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # front stays the same and items are added to the tail
        # want to compare the length of storage to the capcaity of the ring
        if self.storage.length < self.capacity:
            # add item to the tail
            self.storage.add_to_tail(item)
            # set current to the tail
            self.current = self.storage.tail
            # if current and tail are the same we know we need to remove from the head and insert new item
        elif self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            # make current location the head
            self.current = self.storage.head
        

    def get(self):
        pass