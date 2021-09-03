def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def dfs(root):
        return dfs(root.left)+[root.val] + dfs(root.right) if root else []
    return dfs(root)[k-1]