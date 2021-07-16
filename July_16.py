#169. Majority Element
def majorityElement(self, nums):
    nums.sort()
    return nums[len(nums)/2]
#time Onlogn space O1


#238. Product of Array Except Self
def productExceptSelf(self, nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    final = [1]*len(nums)
    for i in range(1,len(nums)):
        left[i]=nums[i-1]*left[i-1]
    for i in range(len(nums)-2,-1,-1):
        right[i]=nums[i+1]*right[i+1]
    for i in range(len(left)):
        final[i] = left[i]*right[i]
    return final
def productExceptSelf(self, nums):
    
    final = [1]*len(nums)
    R=1
    for i in range(1,len(nums)):
        final[i]=nums[i-1]*final[i-1]
    for i in range(len(nums)-1,-1,-1):
        final[i] *=R
        R *= nums[i]

    return final

#time on space o1

def findDuplicate(self, nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=0
        else:
            return i

#time on space on

def findDuplicate(nums):
    slow = 0
    fast = 0
    slow2 =0
    while True:
        slow =nums[slow]
        
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow2 == slow:
            return slow2
findDuplicate([1,3,4,2,2])


#time on space o1