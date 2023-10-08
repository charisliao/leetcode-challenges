# Date created: 10/8/2023 
# leetcode no. 344 - Reverse String 
# Difficulty: Easy 

# Problem Statement:
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

from typing import List

# My Solution
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    
    left, right = 0, len(s)-1
    
    while left < right: 
        left_item = s[left]
        right_item = s[right]
        s[left] = right_item 
        s[right] = left_item 
        left += 1 
        right -= 1 
    
    return s


if __name__ == "__main__" :

    # test case 1 
    s = ["h","e","l","l","o"]
    print(reverseString(s))
    
    # test case 2
    s = ["H","a","n","n","a","h"]
    print(reverseString(s))