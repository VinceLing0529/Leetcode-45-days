
#48. Rotate Image
def rotate(self, matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[j][i],matrix[i][j]=matrix[i][j], matrix[j][i]     
    for i in range(n):
        matrix[i]=matrix[i][::-1]
    return matrix

#79. Word Search
def exist(self, board, word):
    row = len(board)
    col = len(board[0])
    index = len(word)
    def search(i,j,current_index):
        if current_index == index:
            return True
        elif 0<=i<row and 0<=j<col and board[i][j]==word[current_index]:
            temp = board[i][j]
            board[i][j]=''
            if search(i-1,j,current_index+1) or search(i+1,j,current_index+1) or search(i,j-1,current_index+1) or search(i,j+1,current_index+1):
                return True
            board[i][j]=temp
        return False
    for i in range(row):
        for j in range(col):
            if board[i][j] ==word[0]  and search(i,j,0):
                return True
    return False
#784. Letter Case Permutation
def letterCasePermutation(self, S):
    """
    :type S: str
    :rtype: List[str]
    """
    if not S:
        return [""]
    index = -1
    for i in range(len(S)):
        if S[i].isalpha():
            index = i
            break
    if index == -1:
        return [S]
    else:
        temp= self.letterCasePermutation(S[index+1:])
        res = []
        for s in temp:
            res.append(S[:index]+S[index].lower()+s)
            res.append(S[:index]+S[index].upper()+s)
        return res