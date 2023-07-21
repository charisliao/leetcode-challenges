# Date created: 7/20/2023 
# Leetcode no. 1299 - Replace Elements with Greatest Element on Right Side
# Difficulty: Easy 
# Language: Python

# Problem Statement:
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

# My attempt:

# While this attempts work for smaller test cases, it exceeded limited with larger 
# test cases, so we need a more optimized solution. 
# Since there are a lot of repeated work comparing array multiple time, the runtime in 
# this solution is O(n^2) 
def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    if len(arr) < 1: 
        return arr 
    else: 
        for i in range(len(arr)-1): 
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr 
    
# To avoid repeated work for comparing array[i] and array[i+1:], we will work in reverse
# order, because if we can get the max value for the next postion, we only need to 
# compare two values instead of a value and an entire array. 
def replaceElementsOptimized(arr):

    rightMax = -1
    for i in range(len(arr)-1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax 
        rightMax = newMax 
    return arr 


    

if __name__ == "__main__":
    #test case 1
    arr = [17,18,5,4,6,1]
    print(replaceElements(arr)) # [18,6,6,6,1,-1]
    arr = [17,18,5,4,6,1]
    print(replaceElementsOptimized(arr))

    #test case 2
    arr = [400]
    print(replaceElements(arr)) # [-1]
    arr = [400]
    print(replaceElementsOptimized(arr))    
