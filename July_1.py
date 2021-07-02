#1.ContainsDublipcate

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

#Time O(N^2)
#Space  O(1)

def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

#Time O(nLOGn)
#Space  O(1)


def containsDuplicate(nums):
    new_dict = {}
    for i in range(len(nums)):
        if nums[i] not in new_dict:
            new_dict[nums[i]]=1
        else:    
            return True
    return False
#Time O(n)
#Space  O(n)



x = [1,2,3,4,6]
y=[1,2,3,1]
print(containsDuplicate(x))
print(containsDuplicate(y))


#2.Missing Number

def missingNumber(self, nums): 
    for i in range(len(nums)+1):
        if i not in nums:
             return i


#Time O(n^2)
#Space  O(n)

def missingNumber(self, nums): 
        nums.sort()
        if nums[-1]!=len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(1,len(nums)):
            expact = nums[i-1]+1
            if nums[i]!=expact:
                return expact

#Time O(nLogn)
#Space  O(n) OR O(1)





def missingNumber(self, nums): 
    nums_set = set(nums)
    for i in range(len(nums)+1):
        if i not in nums_set:
            return i
        

#Time O(n)
#Space  O(n) 


def missingNumber(self, nums): 
    allSum = sum(nums)
    expect = 0
    for i in range(len(nums) + 1):
        expect += i
    return expect - allSum

#Time O(n)
#Space  O(1) 

#3.Find All Numbers Disappeared in an Array

def findDisappearedNumbers(self, nums):
    miss = []
    nums_set = set(nums)
    for i in range(1,len(nums)+1):
        if i not in nums_set:
            miss.append(i)
    return miss
#Time O(n)
#Space O(1)