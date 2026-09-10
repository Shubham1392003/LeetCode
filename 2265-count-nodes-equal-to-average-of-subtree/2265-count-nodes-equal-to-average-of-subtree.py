# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0

        def sub(node):
            if not node:
                return 
            if node.val ==avg(node)[0]//avg(node)[1]:
                self.ans+=1
            sub(node.left)
            sub(node.right)
            
        def avg(node):
            if not node:
                return 0,0
            l,lc=avg(node.left)
            r,rc=avg(node.right)
            return l+r+node.val , lc+rc+1
        sub(root)
        return self.ans
    
