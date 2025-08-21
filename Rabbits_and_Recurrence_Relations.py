"""
#Rabbits and Recurrence Relations
Given: Positive integers n≤40 and k≤5

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

def rabbits(n, k):
    if n==1 or n == 2:
        return 1
    dp = [0]*(n+1)
    dp[1], dp[2] = 1,1
    for i in range(3, )