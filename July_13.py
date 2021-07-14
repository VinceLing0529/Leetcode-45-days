#100. same tree

def isSameTree(self, p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 

#Time On
#sPACE O LOGN IF BALANCED ON IF UNBLANACED

#112.path su'm
def hasPathSum(self, root, targetSum):
    if not root:
        return False
    elif not root.left and not root.right:
        return root.val == targetSum
    else:
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
#Time On
#sPACE O LOGN IF BALANCED ON IF UNBLANACED

#543Diameter of Binary Tree

#543.Diameter of binary tree
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left =dfs(root.left)
            right =dfs(root.right)
            res[0] = max(res[0],2+left +right)
            return 1 + max(left,right)
        dfs(root)
        return res[0]
#Time On
#sPACE O LOGN IF BALANCED ON IF UNBLANACED

#617
def mergeTrees(self, root1, root2):
    if root1 == None:
        return root2
    if root2 == None:
        return root1
    root1.val+=root2.val
    root1.left = self.mergeTrees(root1.left,root2.left)
    root1.right = self.mergeTrees(root1.right,root2.right)
    return root1
#Time O m of node
#sPACE O LOGm IF BALANCED Om IF UNBLANACED

#104Minimum Depth of Binary Tree

def maxDepth(self, root):
    if root == None:
        return 0
    queue = deque()
    queue.append((root,1))
    while queue:
        node, depth = queue.popleft()
        if node.left:
            queue.append((node.left,depth+1))
        if node.right:
            queue.append((node.right,depth+1))
    return depth

#time o n
#space om 

#235Lowest Common Ancestor of a Binary Search Tree
def lowestCommonAncestor(self, root, p, q):

    parent_val = root.val

    p_val = p.val

    q_val = q.val

    if p_val > parent_val and q_val > parent_val:    
        
        return self.lowestCommonAncestor(root.right, p, q)
    
    elif p_val < parent_val and q_val < parent_val:    
        
        return self.lowestCommonAncestor(root.left, p, q)
    
    else:
        return root


#time o n of node
#space o n hight