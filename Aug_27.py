#105. Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder : return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:mid +1],inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
    return root

#98. Validate Binary Search Tree
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(root,left,right):
        if not root : return True
        if not (root.val < right and root.val > left) : return False
        return dfs(root.left, left,root.val) and dfs(root.right,root.val,right)
    return dfs(root,-2147483649,2**31)