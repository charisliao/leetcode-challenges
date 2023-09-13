# Date: 9/12/2023
# Leetcode no.283 Move zeros 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10**4
# -2**31 <= nums[i] <= 2**31 - 1

from typing import List
# My solution:

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeros = nums.count(0)
    writerPointer = 0 
    for i in range(len(nums)):
        if nums[i] != 0: 
            nums[writerPointer] = nums[i]
            writerPointer += 1
        if i >= len(nums) - zeros:
            nums[i] = 0 
    return nums
                

if __name__ == "__main__":

    #test case 1 
    nums = [0,1,0,3,12]
    print(moveZeroes(nums)) # [1,3,12,0,0]

    #test case 2
    nums = [0]
    print(moveZeroes(nums)) # [0]

    