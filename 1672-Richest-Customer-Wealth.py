# Date: 8/19/2023 
# Leetcode no.1672 Richest Customer Wealth
# Difficulty: Easy

# Problem Statement:
# You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the ith customer has in the jth bank.
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

# Example 1:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each,
# so return 6.

# Example 2:
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10

# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

import numpy as np

def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    maxWealth = 0 
    for i in range(len(accounts)):
        np_account = np.array(accounts[i])
        maxWealth = max(maxWealth, sum(np_account))
    return maxWealth 

if __name__ == "__main__":
    # test case 1
    accounts = [[1,2,3],[3,2,1]]
    print(maximumWealth(accounts)) # 6

    # test case 2
    accounts = [[1,5],[7,3],[3,5]]
    print(maximumWealth(accounts)) # 10

    # test case 3
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    print(maximumWealth(accounts)) # 17

    


