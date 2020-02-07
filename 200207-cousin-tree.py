class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    # Fill this in.
    return [0]

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
