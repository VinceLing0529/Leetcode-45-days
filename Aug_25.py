#451. Sort Characters By Frequency

def frequencySort(self, s: str) -> str:
    counter = Counter(s)
    heap = []
    for key in counter:
        heapq.heappush(heap,(-counter[key],key))
    fresort = []
    while heap:
        heapEle = heapq.heappop(heap)
        fresort.append(heapEle[1]*-heapEle[0])
    return ''.join(fresort)
#215. Kth Largest Element in an Array

def findKthLargest(self, nums: List[int], k: int) -> int:
    if k == len(nums):
        return min(nums)
    if k == 1:
        return max(nums)
    return heapq.nlargest(k,nums)[-1]
#767. Reorganize String

def reorganizeString(self, s: str) -> str:
    counter = Counter(s)
    maxheap = []
    result = []
    last = None
    for k,v in counter.items():
        heappush(maxheap,[-v,k])
    while maxheap:
        item = heappop(maxheap)
        v,k = -item[0],item[1]
        result +=k
        v-=1
        if last : heappush(maxheap,last)
        if v>0 : last = [-v,k]
        else: last = None
    return ''.join(result) if len(result) == len(s) else ''

#116. Populating Next Right Pointers in Each Node
def connect(self, root: 'Node') -> 'Node':
    if not root : return root
    q = [[root]]
    while q[0]:
        node= q.pop(0)
        m = []
        pre = None
        for item in node :
            item.next = pre
            pre = item
            if item.right !=None:
                m.append(item.right)
            if item.left != None:
                m.append(item.left)
        q.append(m)
    return root
117 same soltion
#199. Binary Tree Right Side View
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    res =  []
    def dfs(root,level):
        if root == None:return
        if level >= len(res):
            res.append(root.val)
        if root.right:
            dfs(root.right,level+1)
        if root.left:
            dfs(root.left,level+1)
    dfs(root,0)
    return res