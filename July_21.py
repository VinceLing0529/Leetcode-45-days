#Subsets
def subsets(self, nums: List[int]) -> List[List[int]]:
    output = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            output.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)
    dfs(0)
    return output
#O N*2^N
#O(N)

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()
    def dfs(start,end,curr):
        output.append(curr[::])
        for i in range(start,end+1):
            if i >start and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            dfs(i+1,end,curr)
            curr.pop()
    dfs(0,len(nums)-1,[])
    return output
#O N*2^N
#O(N)

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    if len(nums)==1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perm = self.permute(nums)
        for j in perm:
            j.append(n)
        res.extend(perm)
        nums.append(n)
    return res
#O N*2^N
#O(N)
