# Date: 9/10/2023 
# Leetcode no. 941. Valid Mountain Array 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an array of integers arr, return true if and only if it is
# a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# my solution:
def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i+1]:
        i += 1

    if i == 0 or i == len(arr) - 1:
        return False

    while i < len(arr) - 1 and arr[i] > arr[i+1]:
        i += 1

    return i == len(arr) - 1

if __name__ == "__main__":
    # test case 1
    arr = [2,1]
    print(validMountainArray(arr)) # False

    # test case 2
    arr = [3,5,5]
    print(validMountainArray(arr)) # False

    # test case 3
    arr = [0,3,2,1]
    print(validMountainArray(arr)) # True