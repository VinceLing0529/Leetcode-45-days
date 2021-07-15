#852.Peak Index in a Mountain Array
def peakIndexInMountainArray(self, arr):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right)/2
        if arr[mid] > arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        if arr[mid] < arr[mid-1] and arr[mid]>arr[mid+1]:
            right = mid -1
        if arr[mid] > arr[mid-1] and arr[mid]<arr[mid+1]:
            left = mid + 1  
            
    return mid
[0,1,0]
#time o logn
#space o1

#637 Average of Levels in Binary Tree
def averageOfLevels(self, root):
    av = []
    queue = deque([root])
    while queue:
        length = len(queue)
        Sum = 0
        for _ in range(length):
            current = queue.popleft()
            Sum += float(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        average = Sum / length
        av.append(average)
    return av
#time o n
#space om
#111.Minimum Depth of Binary Tree
def minDepth(self, root):
    if root == None:
        return 0
    queue = deque()
    queue.append((root,1))
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left,depth+1))
        if node.right:
            queue.append((node.right,depth+1))
#time o n
#space om 