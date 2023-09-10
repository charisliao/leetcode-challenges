# Date: 9/10/2023
# Leetcode no.26 Remove Duplicates from Sorted Array
# Difficulty: Easy

# Problem Statement:
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears
# only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, 
# to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain
# the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of
# nums.
# Return k.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).

# Constraints:
# 0 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100

from typing import List
# My Solution
def removeDuplicates(nums: List[int]) -> int:

    # There's no need to create an extra set that takes up memory space 
    # unique = set()
    # writer = 0 
    # for i in range(len(nums)):
    #     if nums[i] not in unique: 
    #         unique.add(nums[i])
    #         nums[writer] = nums[i]
    #         writer += 1

    # nums is already a sorted array 

    writer = 1 
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1] : 
            nums[writer] = nums[i]
            writer += 1
            
    return writer 
            
    return writer 

if __name__ == "__main__":
    # test case 1 
    nums = [1,1,2]
    print(removeDuplicates(nums)) # 2

    # test case 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums)) # 5



