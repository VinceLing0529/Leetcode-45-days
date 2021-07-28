#198. House Robber
def rob(self, nums: List[int]) -> int:
    rob1,rob2= 0, 0
    for n in nums:
        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

#213. House Robber II
def rob(self, nums: List[int]) -> int:
    
    def help(num):
        rob1, rob2 = 0 , 0
        for i in num:
            temp = max(rob1 + i, rob2 )
            rob1 = rob2
            rob2 = temp
        return rob2
    return max(nums[0],help(nums[1:]),help(nums[:-1]))
#322. Coin Change
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1]*(amount +1)
    dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if a - c >=0:
                dp[a] = min(dp[a],1+dp[a-c])
    return dp[amount] if dp[amount]!= amount +1 else -1