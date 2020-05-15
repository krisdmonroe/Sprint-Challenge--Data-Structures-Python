from reverse import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = LinkedList()

    def append(self, item):
        # # front stays the same and items are added to the tail
        # # want to compare the length of storage to the capcaity of the ring
        # if self.storage.length < self.capacity:
        #     # add item to the tail
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.tail
        # if self.storage.length == 1:
        #     self.current = self.storage.head
        # else:
        #     if self.capacity > self.storage.length:
        #         self.storage.add_to_tail(item)

        #     elif self.current == self.storage.tail:
        #         self.storage.remove_from_head()
        #         self.storage.add_to_head(item)
        #     # make current the head
        #         self.current = self.storage.head
        # Above not working going to try something else
        # if self.storage.length < self.capacity:
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.tail
        # else:
        #     if self.current == self.storage.tail:
        #         self.storage.remove_from_head()
        #         self.storage.add_to_head(item)
        #         self.current = self.storage.head
        # if self.capacity > self.storage.length:
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.tail
        # else:
        #     if self.current != self.storage.tail:
        #         self.current = self.storage.head
        #     else:
        #         self.current = self.storage.head
        # ---------------------------------------------
        # if self.storage.length < self.capacity:
        #     self.storage.add_to_tail(item)
        # else:
        #     if self.current == None:
        #         self.current = self.storage.head
        #     elif self.current.next == None:
        #         self.current = self.storage.head
        #     else:
        #         self.current = self.current.next
        #     self.current.value = item
        if self.storage.length < self.capacity:
            self.storage.add_to_end(item)
        else:
            if self.current == None:
                self.current = self.storage.head
            elif self.storage.length == self.capacity:
                self.storage.remove_from_head()
                self.storage.add_to_end(item)
            else:
                node = self.storage.head 
                node.get_next()
            self.current.value = item
        
    def get(self):
        buffer = []
        # makes a variable to make while loop go
        node = self.storage.head
        # while something
        while node:
            # add into buffer the value of the node
            buffer.append(node.get_value())
            # continue the loop
            node = node.get_next()
        return buffer