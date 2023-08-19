# Date: 08/18/2023
# Leetcode no. 2236 - Root Equals Sum of Children
# Difficulty: Easy 

# Problem Statement:
# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# Example:
# Input: root = [10,4,6]
# Output: true
# Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
# 10 is equal to 4 + 6, so we return true.

# Example2:
# Input: root = [5,3,1]
# Output: false
# Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
# 5 is not equal to 3 + 1, so we return false.

# Constraints:
# The tree consists only of the root, its left child, and its right child.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    return root.val == root.left.val + root.right.val


if __name__ == "__main__":
    # test case 1
    root1 = TreeNode(10)
    root1.left = TreeNode(4)
    root1.right = TreeNode(6)
    print(checkTree(root1)) # true

    # test case 2
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(1)
    print(checkTree(root2)) # false
