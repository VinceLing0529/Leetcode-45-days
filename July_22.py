#47. Permutations II
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    perm = []
    count = {n:0 for n in nums}
    for n in nums:
        count[n] +=1
    def dfs():
        if len(perm)==len(nums):
            res.append(perm.copy())
            return
        for n in count:
            if count[n]>0:
                perm.append(n)
                count[n]-=1
                dfs()
                count[n]+=1
                perm.pop()
    dfs()
    return res
#77. Combinations
def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    com = []
    def dfs(i):
        if len(com) == k:
            res.append(com.copy())
            return
        for i in range(i,n+1):
            com.append(i)
            dfs(i+1)
            com.pop()
    dfs(1)
    return res
#39. Combination Sum
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def dfs(i,curr,total):
        if total == target:
            res.append(curr.copy())
            return
        
        if i>= len(candidates) or total > target:
            return
        
        curr.append(candidates[i])
        dfs(i,curr,total +candidates[i])
        curr.pop()
        dfs(i+1,curr,total)
        
        

    dfs(0,[],0)
    return res
                