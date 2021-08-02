#377. Combination Sum IV

def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = {0:1}
    for total in range(1,target+1):
        dp[total]=0
        for n in nums:
            dp[total] += dp.get(total-n,0)
            
    
    return dp[target]
#91. Decode Ways
def numDecodings(self, s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(1, n):
        if s[i] != '0':
            dp[i+1] += dp[i]
        if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
            dp[i+1] += dp[i-1]
    return dp[n]
#55. Jump Game
def canJump(self, nums: List[int]) -> bool:
    last = len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i  + nums[i] >= last:
            last = i
    return last==0

#647. Palindromic Substrings

def countSubstrings(self, s: str) -> int:
    res = 0
    for i in range(len(s)):
        l = r = i
        while l >=0 and r <len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
        l,r = i, i +1
        while l >=0 and  r <len(s) and s[l] == s[r]:
            res +=1
            l-=1
            r+=1
    return res