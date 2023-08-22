# Date: 08/21/2023
# Leetcode no. 383 - Ransom Note
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given two stings ransomNote and magazine, return true if ransomNote can
# be constructed from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# My Approach:
from collections import Counter 
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    note = Counter(ransomNote)
    mag = Counter(magazine)

    for note in ransomNote: 
        if note not in mag.keys() or mag[note] == 0:
            return False 
        else: 
            mag[note] -= 1            
    return True

if __name__ == "__main__":
    
    # test case 1
    # expected output: True
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))

    # test case 2
    # expected output: False
    ransomNote = "aa"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine))

