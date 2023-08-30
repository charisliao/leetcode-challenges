# Date: 08/30/2023
# Leetcode no. 1295 - Find Numbers with Even Number of Digits
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an array nums of integers, return how many of them contain an even number of digits.

# Example:
# Input: nums = [12,345,2,6,7896]
# Output: 2

# Input: nums = [555,901,482,1771]
# Output: 1

# My Approach:
from typing import List
def findNumbers(nums: List[int]) -> int:
    count = 0 
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1 
    return count


if __name__ == "__main__":
        
    # test case 1
    # expected output: 2
    nums = [12,345,2,6,7896]
    print(findNumbers(nums))
    
    # test case 2
    # expected output: 1
    nums = [555,901,482,1771]
    print(findNumbers(nums))