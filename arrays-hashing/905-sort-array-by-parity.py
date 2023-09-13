# Date: 9/12/2023
# Leetcode no. 905 Sort Array By Parity 
# Difficulty: Easy
# Language: Python


# Problem Statement:
# Given an array nums of non-negative integers, return an array consisting
# of all the even elements of nums, followed by all the odd elements of nums.

# You may return any answer array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]

# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3]
# would also be accepted.

from typing import List

# My solution:
def sortArrayByParity(nums: List[int]) -> List[int]:
        
    left, right = 0, len(nums)-1 
    
    while left < right: 
        if nums[left] % 2 != 0 and nums[right] % 2 == 0: 
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp 
            right -= 1
            left += 1 
        if nums[right] % 2 != 0: 
            right -= 1
        if nums[left] % 2 == 0: 
            left += 1 
    return nums 
        

if __name__ == "__main__":

    #test case 1 
    nums = [3,1,2,4]
    print(sortArrayByParity(nums)) # [2,4,3,1]

    #test case 2
    nums = [0]
    print(sortArrayByParity(nums)) # [0]

    
