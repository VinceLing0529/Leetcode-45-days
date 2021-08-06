#133. Clone Graph
def cloneGraph(self, node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew :
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node]=copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node) if node else None
#417. Pacific Atlantic Water Flow 
def pacificAtlantic(self, heights):
    ROWS, COLS = len(heights),len(heights[0])
    pac,atl = set(),set()
    res = []
    def dfs(r,c,visit,prevHeight):
        if ((r,c) in visit or r<0 or c<0 or r == ROWS or c ==COLS or heights[r][c] < prevHeight):
            return
        visit.add((r,c))
        dfs(r+1,c,visit,heights[r][c])
        dfs(r-1,c,visit,heights[r][c])
        dfs(r,c+1,visit,heights[r][c])
        dfs(r,c-1,visit,heights[r][c])
    for c in range(COLS):
        dfs(0,c,pac,heights[0][c])
        dfs(ROWS-1,c,atl,heights[ROWS-1][c])
    for r in range(ROWS):
        dfs(r,0,pac,heights[r][0])
        dfs(r,COLS-1,atl,heights[r][COLS-1])
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])
    return res

#Num of island
def numIslands(self, grid):
    if not grid: return 0
    row,col = len(grid),len(grid[0])
    island = 0
    
    def change(i,j):
        if grid[i][j] == "1":
            grid[i][j] = "0"
            if i-1 >=0:
                change(i-1,j)
            if j -1 >=0:
                change(i,j-1)
            if i+1 < len(grid):
                change(i+1,j)
            if j+1 < len(grid[0]):
                change(i,j+1)
            
            
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                island +=1
                change(i,j)

    return island