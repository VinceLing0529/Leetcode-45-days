
#442. Find All Duplicates in an Array


def findDuplicates(self, nums):
    li = []
    for i in range(len(nums)):
        index = abs(nums[i])-1
        if nums[index]<0:
            li.append(index+1)
        nums[index]=-nums[index]
    return li

#Time On Space O1

#73. Set Matrix Zeroes
def setZeroes(self, matrix):
    r = len(matrix)
    c = len(matrix[0])
    row,col = set(),set()
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                row.add(i)
                col.add(j)
    for i in range(r):
        for j in range(c):
            if i in row or j in col:
                matrix[i][j]=0
    return matrix
#Time O(m*n) Space O(m+n)

#73. Spiral Matrix
def spiralOrder(self, matrix):
    r = len(matrix)
    c = len(matrix[0])
    li = []
    top = 0
    bot = r-1
    left = 0
    right = c -1
    size = r*c
    while(len(li) < size):
        for i in range(left,right+1):
            if (len(li) < size):
                li.append(matrix[top][i])   
        top +=1
        
        for i in range(top,bot+1):
            if (len(li) < size):
                li.append(matrix[i][right])
        right -=1
        
        for i in range(right,left-1,-1):
            if (len(li) < size):
                li.append(matrix[bot][i])
        bot-=1
        
        for i in range(bot,top-1,-1):
            if (len(li) < size):
                li.append(matrix[i][left])
        left +=1
        
    return li
#Time O(m*n) Space O(m+n)
