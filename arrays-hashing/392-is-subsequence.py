# Date created: 7/21/2023 
# Leetcode no. 392 Is Subsequence 
# Difficulty: Easy 
# Language: Python

# Problem Statement: 
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# example 1: 
# Input: s = "abc", t = "ahbgdc"
# Output: true

# example 2: 
# Input: s = "axc", t = "ahbgdc"
# Output: false


# My Solution 
# I used two pointers to solve this problem. 
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    left, right = 0, 0 
    if len(s) > len(t):
        return False 
    while left < len(s) and right < len(t):
        if s[left] == t[right]: 
            left += 1
        right += 1
    return left == len(s) 

if __name__ == "__main__":

# test case 1
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t)) # True

# test case 2
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t)) # False

# test case 3
    s = "b"
    t = "c" 
    print(isSubsequence(s, t)) # False

