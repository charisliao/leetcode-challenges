 # Date: 08/20/2023
# Leetcode no. 412 - Fizz Buzz
# Difficulty: Easy
# Language: Python

# Problem Statement:
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 
# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Constraints:
# 1 <= n <= 104

# My attempt:
def fizzBuzz(n):
    arr = [0] * (n)
    for i in range(0, n):
        position = i+1
        if position % 3 == 0 and position % 5 == 0:
            arr[i] = "FizzBuzz"
        elif position % 3 == 0: 
            arr[i] = "Fizz"
        elif position % 5 == 0:
            arr[i] = "Buzz"
        else: 
            arr[i] = str(position)
    return arr 

if __name__ == "__main__":
    # test case 1
    n = 3
    print(fizzBuzz(n)) # ["1","2","Fizz"]

    # test case 2
    n = 5
    print(fizzBuzz(n)) # ["1","2","Fizz","4","Buzz"]

    # test case 3
    n = 15
    print(fizzBuzz(n)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]