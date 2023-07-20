# Leetcode no. 217 - Contains Duplicate 
# Difficulty: Easy
# Language: Python

# Problem Statement: 
# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example:
# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# My attempt: 
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
    
if __name__ == "__main__":

    # test case 1
    nums = [1,2,3,1]
    print(containsDuplicate(nums)) # True

    # test case 2
    nums = [1,2,3,4]
    print(containsDuplicate(nums)) # False

    # test case 3
    nums = [1]
    print(containsDuplicate(nums)) # False

    # test case 4
    nums = [1,1,1,3,3,4,3,2,4,2] # True
    print(containsDuplicate(nums))

