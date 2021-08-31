#15. 3Sum

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    add =set()
    res = []
    for i in range(len(nums)-1,-1,-1):
        last = nums[i]
        start,end = 0,i-1
        while start < end:
            s = last + nums[start] +nums[end]
            if s == 0:
                if (last,nums[start],nums[end]) not in add : res.append([last,nums[start],nums[end]])
                add.add((last,nums[start],nums[end]))
                start +=1
            elif s> 0:
                end -=1
            else:
                start +=1
    return res
#16 3 sum closest:
def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    close = 1000
    for i in range(len(nums)):
        left = i +1
        right = len(nums) -1
        while left < right:
            if nums[left] + nums[right] + nums[i] == target:
                return target
            if abs(target - (nums[left] +nums[right] +nums[i])) < abs(target-close):
                close = nums[left] +nums[right]+nums[i]
            if nums[left] + nums[right] +nums[i] < target:
                left +=1
            else:
                right -=1

    return close
#713. Subarray Product Less Than K
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <=1:
        return 0
    
    res = 0
    pro = 1
    left = 0
    right = 0
    
    while right < len(nums):
        pro *=nums[right]
        while pro >= k:
            pro /= nums[left]
            left +=1
        res += right - left +1
        right +=1
        
    return res