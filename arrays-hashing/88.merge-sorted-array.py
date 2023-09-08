# Date: 09/07/2023
# Leetcode no.88 Merge Sorted Array 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3   
#        nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1
#        nums2 = [],  n = 0
# Output: [1]

# Explanation: The arrays we are merging are [1] and [].

# The result of the merge is [1].

# My Solution
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead. 
    """

    pointer1 = m-1
    pointer2 = n-1

    for pointer in range(m+n-1, -1, -1):
        if pointer2 < 0:
            break 
        if pointer1 > 0 and nums1[pointer1] > nums2[pointer2]:
            nums1[pointer] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[pointer] = nums2[pointer2]
            pointer2 -= 1

    return nums1


if __name__ == "__main__":
    # test case 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(merge(nums1, m, nums2, n))  # [1,2,2,3,5,6]

    # test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(merge(nums1, m, nums2, n))  # [1]

    # test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(merge(nums1, m, nums2, n))  # [1]
    