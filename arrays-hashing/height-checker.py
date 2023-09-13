# Date: 9/13/2023
# Leetcode Height Checker - no leetcode number 
# Difficulty: Easy
# Language: Python

# Problem Statement:
# A school is trying to take an annual photo of all the students. 
# The students are asked to stand in a single file line in non-decreasing 
# order by height. Let this ordering be represented by the integer array 
# expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that 
# the students are standing in. Each heights[i] is the height of the ith 
# student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].

# Example 1:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]

# Example 2:
# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]

# Example 3:
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]

# My solution:
def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    expected = sorted(heights)
    count = 0 
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count

if __name__ == "__main__":
    # test case 1
    heights = [1,1,4,2,1,3]
    print(heightChecker(heights)) # 3

    # test case 2
    heights = [5,1,2,3,4]
    print(heightChecker(heights)) # 5

    # test case 3
    heights = [1,2,3,4,5]
    print(heightChecker(heights)) # 0

    