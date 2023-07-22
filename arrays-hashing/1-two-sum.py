# Date created: 7/21/2023 
# Leetcode no. two sum  
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

# My attempt:
def twoSum(nums, target):
    location = {}
    for i in range(len(nums)):
        if nums[i] not in location: 
            location[nums[i]] = i 
        if target - nums[i] in location and location[target-nums[i]] != i: 
            return [i, location[target-nums[i]]]
        
if __name__ == "__main__":

    # test case 1
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target)) # [0,1]

    # test case 2
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target)) # [1,2]

    # test case 3
    nums = [3,3]
    target = 6
    print(twoSum(nums, target)) # [0,1]

    