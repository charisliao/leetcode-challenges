# Date created: 7/21/2023 
# Leetcode no. Length of Last Word 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example:
# Input: s = "Hello World"
# Output: 5

# Input: s = "   fly me   to   the moon  "
# Output: 4

# Input: s = "luffy is still joyboy"
# Output: 6

# My attempt:
def lengthOfLastWord(s):
    return len(s.split()[-1])


if __name__ == "__main__":
    
    #test case 1
    s = "Hello World"
    print(lengthOfLastWord(s)) # 5

    #test case 2
    s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s)) # 4

    #test case 3
    s = "luffy is still joyboy"
    print(lengthOfLastWord(s)) # 6
