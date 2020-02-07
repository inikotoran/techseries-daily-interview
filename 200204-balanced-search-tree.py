class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def create_height_balanced_bst(nums):
    # Fill this in.
    if (len(nums) == 3):
        n = Node(nums[1])
        n.left = nums[0]
        n.left = nums[2]
        return n
    if (len(nums) == 2):
        n = Node(nums[1])
        n.left = nums[0]
        return n
    if (len(nums) == 1):
        return Node(nums[0])

    center = 0
    if len(nums) % 2 == 0:
        center = nums[(len(nums) + 1) / 2]
    if len(nums) % 2 == 1:
        center = nums[(len(nums)) / 2]

    left = nums[0:center-1]
    right = nums[center:len(nums)]

    bst = Node(center)
    bst.left = create_height_balanced_bst(left)
    bst.right = create_height_balanced_bst(right)

    return bst


tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
print(tree)
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
