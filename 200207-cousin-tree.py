class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def node_depth(self, tree, val, depth):
    if (tree == None):
      return 0
    if (tree.value == val):
      return depth
    depth += 1
    return self.node_depth(tree.left, val, depth) + self.node_depth(tree.right, val, depth)
  
  def find_all_cousins(self, tree, depth, val, current_depth):
    if (current_depth == depth and tree.value != val):
      return [tree.value]
    
    result = []
    lefty = None
    righty = None

    if (tree != None and tree.left != None):
      lefty = self.find_all_cousins(tree.left, depth, val, current_depth+1)
    if (tree != None and tree.right != None):
      righty = self.find_all_cousins(tree.right, depth, val, current_depth+1)
    
    if (lefty != None): 
      result.extend(lefty)
    if (righty != None): 
      result.extend(righty)

    return result

  def list_cousins(self, tree, val):
    # Fill this in.
    # find the node. how?
    # find the cousin = same depth
    # find the depth of node
    depth = self.node_depth(tree, val, 0)
    return self.find_all_cousins(tree, depth, val, 0)

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]
