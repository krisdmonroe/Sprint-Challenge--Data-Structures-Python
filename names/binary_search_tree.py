from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # NO RETURNS BEACUSE WE DO NOT NEED TO SEND THE DATA BACK UP THE TREE
        # self will be the root of the tree
        # value greater
        if value >= self.value:
            # if we reach the end
            if self.right is None:
                # add the value to the search tree
                self.right = BinarySearchTree(value)
            else:
                # search through itself again with recursion
                self.right.insert(value)
        # value less then
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if self.right is None:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call fn and initate it with the value of that node wich in this case is self.value
        fn(self.value)
        # keep going with the for_each until the left is none and then stop
        if self.left is not None:
            self.left.for_each(fn)
        # keep going with the for_each until the right is none and then stop
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Inorder Traversal (Left-Root-Right)
    def in_order_print(self, node):
        if node is None:
            return
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        # keep going with the for_each until the right is none and then stop
        if node.right is not None:
            self.in_order_print(node.right)
        
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()

        # add the root node
        queue.append(node)

        # loop so long as the stack still has elements 
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            print(current.value)

    #        # Depth-First traversal 
    # # LIFO ordering of the tree elements 

    # def breadth_first_for_each(self, fn):
    #     queue = deque()

    #     # add the root node
    #     queue.append(self)

    #     # loop so long as the stack still has elements 
    #     while len(queue) > 0:
    #         current = queue.popleft()
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)

    #         fn(current.value)
        
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        # keep going with the for_each until the right is none and then stop
        if node.right is not None:
            self.dft_print(node.right)
        if node.left is not None:
            self.dft_print(node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # Preorder Traversal (Root-Left-Right)
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        # keep going with the for_each until the right is none and then stop
        if node.right is not None:
            self.pre_order_dft(node.right)
        

    # Print Post-order recursive DFT
    # Postorder Traversal (Left-Right-Root)
    def post_order_dft(self, node):
        if node.left is not None:
            self.post_order_dft(node.left)
        # keep going with the for_each until the right is none and then stop
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)

