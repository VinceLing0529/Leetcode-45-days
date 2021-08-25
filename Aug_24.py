#567. Permutation in String
def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_count, s2_count = Counter(s1), Counter(s2[:len(s1)])
    print(s1_count,s2_count)
    for i in range(len(s2)-len(s1)):
        if s1_count == s2_count: return True
        
        if s2_count[s2[i]] == 1: 
            del s2_count[s2[i]]
        else: 
            s2_count[s2[i]] -= 1
        
        if s2[i+len(s1)] in s2_count: 
            s2_count[s2[i+len(s1)]] += 1
        else: 
            s2_count[s2[i+len(s1)]] = 1
            
    return s1_count == s2_count

    return False
#424. Longest Repeating Character Replacement
def characterReplacement(self, s: str, k: int) -> int:
    res = 0
    left = 0
    count = {}
    maxf = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right],0)
        maxf = max(maxf, count[s[right]])

        while (right-left+1) - maxf > k:
            count[s[left]] -= 1
            left+=1
        res = max(res, right-left+1)
    return(res)    
#3
def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    end  = 0
    max1 = 0
    d = {}
    while end < len(s):
        if s[end] in d and d[s[end]]>=start:
            start = d[s[end]]+1
        max1 = max(max1,end - start +1)
        d[s[end]] = end
        end +=1
    return max1