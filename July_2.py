#1.Single number

def singleNumber(self, nums):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for i in dict:
        if dict[i]==1:
            return i

#Time O(n)
#Space O(n)

#2.Climbing stairs
def climbStairs(self, n):
    if n==1: 
        return 1
    dp=[1]*(n+1) 
    #dp[1]=1
    #dp[2]=2
    #dp[3]=3
    #dp[4]=5
    #dp[5]=8
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
        if i == n:
            return dp[i]

#Time O(n)
#Space O(n)

#3.Best time to buy stock
def maxProfit(self, prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<prices[j] and prices[j]-prices[i]>profit:
                profit = prices[j]-prices[i]
    return profit

#Time O(n^2)
#Space O(1)

def maxProfit(self, prices):
    profit = 0
    buy = prices[0]
    for i in prices:
        if i<buy:
            buy = i
        elif profit<i-buy:
            profit = i-buy
    return profit
    
#Time O(n)
#Space O(1)