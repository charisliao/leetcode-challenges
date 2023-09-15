# Date: 9/14/2023
# Leetcode no. 448 Find All Numbers Disappeared in an Array 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# My solution:
def findDisappearedNumbers(nums):
    missing = []
    unique = set(nums)

    for i in range(len(nums)):
        if (i+1) not in unique:
            missing.append(i+1)

    return missing

if __name__ == "__main__":

    # test case 1
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums)) # [5,6]

    # test case 2
    nums = [1,1]
    print(findDisappearedNumbers(nums)) # [2]