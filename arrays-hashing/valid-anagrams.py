# Date created: 7/19/2023 
# Leetcode no. 242 Valid Anagrams 
# Difficulty: Easy 
# Language: Python

# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    
    #test case 1
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t)) # True

    #test case 2
    s = "rat"
    t = "car"
    print(isAnagram(s, t)) # False

    #test case 3
    s = "a"
    t = "ab"
    print(isAnagram(s, t)) # False