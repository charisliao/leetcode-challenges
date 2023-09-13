# Date: 9/13/2023
# Leetcode no. 487 Max Consecutive Ones II
# Difficulty: Medium
# Language: Python

# Problem Statement:
# Given a binary array nums, return the maximum number of consecutive 1's
# in the array if you can flip at most one 0.

# Example 1:
# Input: nums = [1,0,1,1,0]
# Output: 4

# Explanation: Flip the first zero will get the maximum number of 
# consecutive 1s.

# After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 4

# My solution:
def findMaxConsecutiveOnes(nums):

    maxCount = 0 
    left, right = 0, 0
    zeroCount = 0 

    while right < len(nums):

        if nums[right] == 0:
            zeroCount += 1 
        
        while zeroCount > 1: 
            if nums[left] == 0: 
                zeroCount -= 1 
            left += 1 

        maxCount = max(maxCount, right - left + 1)
        right += 1
    
    return maxCount

if __name__ == "__main__":

    # test case 1
    nums = [1,0,1,1,0]
    print(findMaxConsecutiveOnes(nums)) # 4

    # test case 2
    nums = [1,0,1,1,0,1]
    print(findMaxConsecutiveOnes(nums)) # 4

    