# Date: Sep 1, 2023
# Leetcode no. 977 Squares of a Sorted Array
# Difficulty: Easy 
# Language: Python

# Problem Statement:
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# My Solution
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return sorted([num ** 2 for num in nums])


if __name__ == "__main__":

    # test case 1
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))  # [0,1,9,16,100]

    # test case 2
    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))  # [4,9,9,49,121]

    # test case 3
    nums = [-1]
    print(sortedSquares(nums))  # [1]