#621. Task Scheduler
def leastInterval(self, tasks, n):
    if n==0:
        return len(tasks)
    l1=len(tasks)
    D=[0]*26
    for i in range(l1):
        D[ord(tasks[i])-65]+=1
    D.sort()
    group=D[25]-1
    idle=group*n
    print(group,idle)
    for i in range(len(D)-1):
        idle-=min(D[24-i],group)
    print(idle)
    if idle<=0:
        return len(tasks)
    return len(tasks)+idle
#452. Minimum Number of Arrows to Burst Balloons
def findMinArrowShots(self, points):
    points.sort()
    l = len(points)
    last_range = points[0]
    count = 1
    for i in range(1,l):
        if points[i][0]<=last_range[1]:
            last_range[0], last_range[1] = min(last_range[1], points[i][0]), min(last_range[1], points[i][1])
        else:
            count+=1
            last_range = points[i]
    return count
#57. Insert Interval
def insert(self, intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    final = []
    for i in intervals:
        if not final or final[-1][1] < i[0]:
            final.append(i)
        else:
            final[-1][1] = max(final[-1][1],i[1])
    return final