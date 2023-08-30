# Date: 08/20/2023
# Leetcode no. 485 - Max Consecutive Ones
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example:
# Input: nums = [1,1,0,1,1,1]
# Output: 3

# Input: nums = [1,0,1,1,0,1]
# Output: 2

from typing import List
# My Approach:
def findMaxConsecutiveOnes(nums: List[int]) -> int:
        count_list = []
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 1: 
                count += 1 
                if i == len(nums)-1:
                    count_list.append(count)
            else: 
                count_list.append(count)
                count = 0 
        # print(count_list)
        return max(count_list)

if __name__ == "__main__":
     
    # test case 1
    # expected output: 3
    nums = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))
    
    # test case 2
    # expected output: 2
    nums = [1,0,1,1,0,1]
    print(findMaxConsecutiveOnes(nums))
