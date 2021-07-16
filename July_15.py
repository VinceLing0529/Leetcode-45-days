#977 Squares of a Sorted Array

def sortedSquares(self, nums):
    new = []
    p = 0
    while(p<len(nums) and nums[p]<0):
        p +=1
    n = p -1
    while(n >=0 and p<len(nums)):
        if (nums[n]*nums[n]) < (nums[p]*nums[p]):
            new.append(nums[n]*nums[n])
            n -=1
        else:
            new.append(nums[p]*nums[p])
            p +=1
    while(n>=0):
        new.append(nums[n]**2)
        n -=1
    while(p<len(nums)):
        new.append(nums[p]**2)
        p+=1
    return new
#Time On Space On
def backspaceCompare(self, s, t):
    def sta(str):
        stack = []
        for i in str:
            if i =="#":
                if stack : stack.pop()
            else:
                stack.append(i)
        return stack
    return sta(s) == sta(t)
#Time OM+N Space OM+N

#720. Longest Word in Dictionary

def longestWord(self, words):
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                ans = word

    return ans