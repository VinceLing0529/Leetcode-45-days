#207. Course Schedule
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i: [] for i in range(numCourses)}
    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        visitSet.remove(crs)
        preMap[crs]= []
        return True
    for crs in range(numCourses):
        if not dfs(crs) : return False
    return True
#210. Course Schedule II
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    top_sort = []

    # # create an adjacency list from the edge list given
    # while doing so, create an indegree record for each vertex/node
    adjacency_list = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)
    for arr in prerequisites:
        child, parent = arr[0], arr[1]

        adjacency_list[parent].append(child)
        indegrees[child] += 1

    # # add all the sources into a queue
    queue = []
    for vertex in range(numCourses):
        if indegrees[vertex] == 0:
            queue.append(vertex)

    # # build top_sort list
    while queue:
        vertex = queue.pop(0)
        top_sort.append(vertex)
        for child in adjacency_list[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)

    # if the length of the sorted list == numCourses, it is possible to complete the courses
    if len(top_sort) == numCourses:
        return top_sort
    return []


def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2 :
        return [x for x in range(n)]
    neighbors = [set() for x in range(n)]
    for start,end in edges :
        neighbors[start].add(end)
        neighbors[end].add(start)
    leaves = []
    for i in range(n):
        if len(neighbors[i]) == 1:
            leaves.append(i)
    remaining_nodes = n
    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        temp = []
        
        for leaf in leaves:
            for neighbor in neighbors[leaf]:
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    temp.append(neighbor)
    
    leaves = temp
    return leaves

#310. Minimum Height Trees
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n<2:
        return range(n)
    
    graph=defaultdict(set)
    indegree=[0]*n
    for u,v in edges:
        graph[u].add(v)
        graph[v].add(u)
        indegree[u]+=1
        indegree[v]+=1
    
    queue=[]
    for i in range(n):
        if indegree[i]==1:
            queue.append(i)
    
    count=n
    
    while count>2:
        new_queue=[]
        
        for current in queue:
            
            for neighbour in graph[current]:
                indegree[neighbour]-=1
                graph[neighbour].remove(current)
                if indegree[neighbour]==1:
                    new_queue.append(neighbour)
            
            count-=1
        queue=new_queue
    
    return queue
#236. Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
        return None
    left_res = self.lowestCommonAncestor(root.left,p,q)
    right_res = self.lowestCommonAncestor(root.right,p,q)
    if (left_res and right_res) or (root in [p,q]):
        return root
    else:
        return left_res or right_res
#654. Maximum Binary Tree
def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    def dfs(nums):
        if len(nums) <1 :
            return None
        max1 = nums.index(max(nums))
        head = TreeNode(nums[max1])
        if max1 > 0 :
            head.left = dfs(nums[0:max1])
        if max1 <len(nums):
            head.right = dfs(nums[max1+1:len(nums)])
        return head
    return dfs(nums)
#662. Maximum Width of Binary Tree
def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    max_width = 0
    root.val = 0
    levels = [root]
    while levels:
        curr_lvl = []
        max_width  = max(max_width,levels[-1].val - levels[0].val +1)
        for node in levels:
            if node.left:
                node.left.val = 2*node.val
                curr_lvl.append(node.left)
            if node.right:
                node.right.val = 2*node.val+1
                curr_lvl.append(node.right)
        levels = curr_lvl
    return max_width