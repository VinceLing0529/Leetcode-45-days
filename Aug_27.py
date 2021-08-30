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

#208. Implement Trie (Prefix Tree)
class Trie:

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = {}

def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    root = self.root
    for i in word:
        if i not in root:
            root[i] = {}
        root = root[i]
    root["end"] = 1
    

def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    root = self.root
    for i in word:
        if i not in root:
            return False
        root = root[i]
    return "end" in root

def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    
    root = self.root
    for i in prefix:
        if i not in root:
            return False
        root = root[i]
    return True
