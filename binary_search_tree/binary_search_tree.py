import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):  # Using a value so key is value.
    self.value = value
    self.left = None
    self.right = None
# 'inset' adds the input value to the binary search tree, adhearing to the
# rules of the ordering of elements in a binary search tree
#Need to traverse th find spot to insert
  def insert(self, value):
    # if value < self.value
    #     if not self.left:
    #         self.left = BinarySearchTree(value)
    #     else:
    #         self.left.insert(value)
    #     else:
    #     if not self.right:
    #         self.right = BinarySearchTree(value)
    #     else:
    #         self.right.insert(value)          

    insert_val = BinarySearchTree(value)
    current_node = self
    placed = False
    while placed == False:
        if value < current_node.value:
            if current_node.left:
                current_node = current_node.left
            else:
                current_node.left = insert_val
                placed = True
        if value >= current_node.value:
            if current_node.right:
                current_node = current_node.right
            else:
                current_node.right = insert_val
                placed = True






  def contains(self, target):
      ### Check if the current value is the target, if so done
    # if self.value == target:
    #     return True
    #   ### Otherwise, left or right based on bigger or smaller and then call contains again
    # else:
    #     if target < self.value:
    #         #go left
    #         if not self.left:
    #             return False
    #         else:
    #             self.left.contains(target)
    #     else:
    #         #go right
    #         if not self.right:
    #             return False
    #         else:
    #             return self.right.contains(target)    
   
    current_node = self
    found = False
    end = False
    while found == False and end == False:
        if target < current_node.value:
            if current_node.left:
                current_node = current_node.left
            else:
                end = True
        if target > current_node.value:
            if current_node.right:
                current_node = current_node.right
            else:
                end = True
        if target == current_node.value:
            found = True
    return found




# get_max returns the maximum value in the binary search tree.
  def get_max(self):
#       ### max node is furthest to the right
#       ### base case:
#       if not self.right:
#           return self.value
#       return self.right.get_max()    

    current_node = self
    end = False
    while end == False:
        if current_node.right:
            current_node = current_node.right
        else:
            end = True
    return current_node.value



# for_each preforms a traversal of _ever_ node in the tree,
#
#


  def for_each(self, cb):
    cb(self.value)

    # if self.value == None:
    #     return
    
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)