#40. Combination Sum II
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []
    def dfs(curr,pos,target):

        if target == 0:
            res.append(curr.copy())
            
        if target <= 0:
            return
        prev = -1
        for i in range(pos,len(candidates)):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            dfs(curr,i+1,target - candidates[i])
            curr.pop()
            prev = candidates[i]
    dfs([],0,target)
    return res
#216. Combination Sum III
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []
    def dfs(i,curr):
        if sum(curr) == n and len(curr)==k :
            res.append(curr.copy())
            return
        for i in range(i,10):
            curr.append(i)
            dfs(i+1,curr)
            curr.pop()
    dfs(1,[])
    return res

#22. Generate Parentheses

def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def dfs(curr="",open = 0,close = 0):
        if len(curr) == n*2:
            res.append(curr)
            return
        if open < n:
            dfs(curr+"(",open+1,close)
        if close < open:
            dfs(curr+")",open,close+1)
        
    
    dfs()
    return res
#494. Target Sum
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    s = sum(nums)
    n, m = len(nums), 2 * s + 1
    if s < target: return 0

    dp = [[0] * m for _ in range(n + 1)]
    dp[0][s] = 1

    for i in range(n):
        for j in range(nums[i], m - nums[i]):
            if dp[i][j]:
                dp[i + 1][j + nums[i]] += dp[i][j]
                dp[i + 1][j - nums[i]] += dp[i][j]
    return dp[-1][s + target] 

#131. Palindrome Partitioning

def partition(self, s: str) -> List[List[str]]:
    res = []
    curr = []
    def dfs(i):
        if i >= len(s):
            res.append(curr.copy())
            return
        for j in range(i,len(s)):
            if self.isPal(s,i,j):
                curr.append(s[i:j+1])
                dfs(j+1)
                curr.pop()
    
    dfs(0)
    return res
def isPal(self,s,l,r):
    while l<r:
        if s[l]!=s[r]:
            return False
        l,r = l+1,r-1
    return True
#17. Letter Combinations of a Phone Number
def letterCombinations(self, digits: str) -> List[str]:
    res = []
    DWL = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    def dfs(i,curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for j in DWL[digits[i]]:
            dfs(i+1,curr+j)
    if digits:
        dfs(0,"")
    return res
                