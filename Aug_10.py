#56. Merge Intervals
def merge(self, intervals):
    if intervals == 1: return intervals
    intervals.sort()
    output = [intervals[0]]
    for start,end in intervals[1:]:

        lastEnd  = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd,end)
        else:
            output.append([start,end])
    return output
#986. Interval List Intersections
def intervalIntersection(self, firstList, secondList):
    ans = []
    i = j = 0
    A = firstList
    B = secondList
    while i < len(firstList) and j < len(secondList):
        low = max(A[i][0],B[j][0])
        hig = min(A[i][1],B[j][1])
        if low <= hig :
            ans.append([low,hig])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return ans

#435. Non-overlapping Intervals
def eraseOverlapIntervals(self, intervals):
    intervals.sort()
    res = 0
    i=0
    while i < len(intervals)-1:
        if intervals[i][1]>intervals[i+1][0]:
            res+=1
            if(intervals[i][1]>intervals[i+1][1]):
                intervals.pop(i)
            else:
                intervals.pop(i+1)
        else:
            i+=1
    return res