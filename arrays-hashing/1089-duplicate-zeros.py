# Date: 9/7/2023 
# Leetcode no. 1089 Duplicate Zeros 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. 
# Do the above modifications to the input array in place and do not return anything.

# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9

# import list
from typing import List

# My Solution
def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    zeros = arr.count(0)
    n = len(arr)
    print(f'zeros: {zeros}')
    print(f'n: {n}')
    for i in range(n-1, -1, -1):
        print(i+zeros)
        if i + zeros < n:
            arr[i+zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1 
            if i + zeros < n: 
                print(f'when arr[i] == 0, i + zero = {i+zeros}')
                arr[i+zeros] = 0 
    return arr


if __name__ == "__main__":

    # test case 1
    arr = [1,0,2,3,0,4,5,0]
    print(duplicateZeros(arr))  # [1,0,0,2,3,0,0,4]

    # test case 2
    arr = [1,2,3]
    print(duplicateZeros(arr))  # [1,2,3]
