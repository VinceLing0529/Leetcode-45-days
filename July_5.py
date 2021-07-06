
#1.maxSubarray
def maxSubArray(self, nums):
    maxSub = nums[0]
    currSum=0
    for n in nums:
        if currSum<0:
            currSum=0
        currSum +=n
        maxSub=max(maxSub,currSum)             
    return maxSub

#time O(n)
#space O(1)


#2.range sum query 
class NumArray(object):

    def __init__(self, nums):
        self.numarray=nums
        
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        sum = 0
        for i in range(left,right+1):
            sum += self.numarray[i]
        return sum
#time On
#Space o1

class NumArray(object):

    def __init__(self, nums):
        self.suma = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.suma[i+1] = self.suma[i]+nums[i]
       
        
        """
        :type nums: List[int]
        """
        

    def sumRange(self, left, right):
        
        return self.suma[right+1]-self.suma[left]
        """
        :type left: int
        :type right: int
        :rtype: int
        """
    
#Time O(1)
#Space O(N)
#3.Counting bits
class Solution(object):
    def countBits(self, n):
        
        dp=[0]*(n+1)
        offset = 1
      
        for i in range(1,n+1):
            if offset *2 ==i:
                offset = i
            dp[i]= 1 +dp[i-offset]
        return dp

#Time(On)
#Space(O1)