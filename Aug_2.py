#416. Partition Equal Subset Sum

def canPartition(self, nums: List[int]) -> bool:
    if sum(nums) % 2 !=0:return False
    dp = set()
    dp.add(0)
    target  = sum(nums)//2
    for i in range(len(nums)-1,-1,-1):
        nextDP =set()
        for t in dp:
            if (t+nums[i])==target:
                return True
            nextDP.add(t+nums[i])
            nextDP.add(t)
        dp = nextDP
    return True if target in dp else False    

#673. Number of Longest Increasing Subsequence
def findNumberOfLIS(self, nums):
    n=len(nums)
    lis=[1]*n
    #lis[i] is the length of LIS having last element as nums[i]
    noOfLIS=[1]*n
    #noOfLIS[i] is the no. of LIS having last element as nums[i]
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]: 
                if lis[j]+1==lis[i]:
                    noOfLIS[i]+=noOfLIS[j]#update by no. of LIS till jth position
                if lis[j]+1>lis[i]:
                    noOfLIS[i]=noOfLIS[j]#set to no. of LIS till jth position
                lis[i]=max(lis[i],lis[j]+1)
    ans=0
    maxi=max(lis)
    for i in range(n):
        if lis[i]==maxi:
            ans+=noOfLIS[i]
    return ans

#698. Partition to K Equal Sum Subsets


def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if  sum(nums)%k !=0 :return False
    def dfs(curr,k,nums):
        if curr > target:
            return False
        if curr == target:
            k -=1
            curr =0
        if not nums:
            return True if not k else False
        for i in range(len(nums)):
            if( dfs( curr + nums[i], k, nums[:i] + nums[i+1:]) ):
                return True
    nums.sort()
    target = sum(nums)//k
    # all numbers must be equal or less than target
    if( nums[-1] > target ): 
        return False
    
    # if you find number directly, decrement k val
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1
    return dfs(0, k, nums[::-1])