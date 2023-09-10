# Date: 9/10/2023
# No leetcode number for this problem. 
# You can find this problem in the Array chapter on leetcode. 

# Problem Statement:
# Given an array arr of integers, check if there exist two indices
# i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Constraints:
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

from typing import List
# My Solution
def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        if arr[i] / 2 in arr[0:i] or arr[i] / 2 in arr[i+1:]:
            return True
        
    return False

if __name__ == "__main__":
    # test case 1
    arr = [10,2,5,3]
    print(checkIfExist(arr)) # True

    # test case 2
    arr = [3,1,7,11]
    print(checkIfExist(arr)) # False