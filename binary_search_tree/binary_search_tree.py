import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)    


        # insert_value = BinarySearchTree(value)
        # inserted = False
        # while inserted == False:
        #     if value < self.value:
        #         if self.left:
        #             self = self.left
        #         else:
        #             self.left = insert_value
        #             inserted = True
        #     if value >= self.value:
        #         if self.right:
        #             self = self.right
        #         else:
        #             self.right = insert_value
        #             inserted = True

    def contains(self, target): 
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)    


        # found = False
        # end = False
        # while found == False and end == False:
        #     if target < self.value:
        #         if self.left:
        #             self = self.left
        #         else:
        #             end = True
        #     if target > self.value:
        #         if self.right:
        #             self = self.right
        #         else:
        #             end = True
        #     if target == self.value:
        #         found = True
        # return found

    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()              


        # end = False
        # while end == False:
        #     if self.right:
        #         self = self.right
        #     else:
        #         end = True
        # return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)