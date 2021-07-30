#152. Maximum Product Subarray
def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    currMin, currMax = 1,1
    for n in nums:
        tem = currMax*n
        currMax = max(n*currMax,n*currMin,n)
        currMin = min(tem,n*currMin,n)
        res = max(res,currMax)
    return res
#300. Longest Increasing Subsequence

def lengthOfLIS(self, nums: List[int]) -> int:
    LIS =[1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i] <nums[j]:
                LIS[i] = max(LIS[i],1+LIS[j])
    return max(LIS)
#5. Longest Palindromic Substring

def longestPalindrome(self, s: str) -> str:
    res= ""
    resLen =0
    for i in range(len(s)):
        l,r = i,i
        while l>= 0 and r <len(s) and s[l] ==s[r]:
            if (r -l +1) >resLen:
                res = s[l:r+1]
                resLen =r -l +1
            l -=1
            r +=1
            
        l,r =i,i+1
        while l>= 0 and r <len(s) and s[l] ==s[r]:
            if (r -l +1) >resLen:
                res = s[l:r+1]
                resLen =r -l +1
            l -=1
            r +=1
    return res