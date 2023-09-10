# Date: 8/18/2023
# Leetcode no. 1480 - Running Sum of 1d Array
# Difficulty: Easy

# Problem Statement:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].


def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums 

if __name__ == "__main__":
    # test case 1
    nums = [1,2,3,4]
    print(runningSum(nums)) # [1,3,6,10]

    # test case 2
    nums = [1,1,1,1,1]
    print(runningSum(nums)) # [1,2,3,4,5]
