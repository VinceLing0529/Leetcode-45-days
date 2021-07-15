#1.Issubtree
def isSubtree(self, root, subroot):
    if not root:return False
    def same(root,subroot):
        if root ==None and subroot ==None:
            return True
        if root ==None or subroot ==None:
            return False
        if root.val!=subroot.val:
            return False
        return same(root.left,subroot.left) and same(root.right,subroot.right)
    
    if root.val == subroot.val and same(root,subroot):
        return True
    return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)

#Invert tree
def invertTree(self, root):
    if root == None:
        return None
    
    left = root.left
    right = root.right
    root.left =right
    root.right = left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
        
#two sum

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
def twoSum(self, nums, target):
    dict = {}
    for i in range(len(nums)):
        if target-nums[i] in dict:
            return [dict[target-nums[i]],i]

        else:
            dict[nums[i]]=i
    return []