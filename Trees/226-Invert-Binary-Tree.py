# Date: 08/18/2023 
# Leetcode no. 226 - Invert Binary Tree 
# Difficulty: Easy

# Problem Statement:
# Given the root of a binary tree, invert the tree, and return its root.

# Example:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root: 
        return None
    right = invertTree(root.right)
    left = invertTree(root.left)
    root.left = right
    root.right = left
    return root 

if __name__ == "__main__":

    # test case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    print(invertTree(root1)) # [4,7,2,9,6,3,1]


    # test case 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print(invertTree(root2)) # [2,3,1]


