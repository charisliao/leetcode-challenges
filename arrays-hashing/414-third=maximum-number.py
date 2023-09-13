# Date: 9/13/2023
# Leetcode no. 414 Third Maximum Number 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an integer array nums, return the third distinct maximum number in
# this array. If the third maximum does not exist, return the maximum number

# Example 1:
# Input: nums = [3,2,1]
# Output: 1

# Explanation: The first distinct maximum is 3.
# The second distinct maximum is 2.

# Example 2:
# Input: nums = [1,2]
# Output: 2

# Explanation: The first distinct maximum is 2.

# My solution 
def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    else:
        nums.sort()
        return nums[-3]
    

if __name__ == "__main__":

    # test case 1
    nums = [3,2,1]
    print(thirdMax(nums)) # 1

    # test case 2
    nums = [1,2]
    print(thirdMax(nums)) # 2
