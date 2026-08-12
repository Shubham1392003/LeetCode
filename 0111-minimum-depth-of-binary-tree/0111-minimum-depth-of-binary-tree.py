# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        count = 0
        minima= float('inf')

        def d(root):

            nonlocal count,minima

            if root is None:
                return 
            
            count +=1

            if root.left is None and root.right is None:
                minima=min(minima,count)
                count -= 1
                return 
            
            d(root.left)
            d(root.right)

            count-=1

        d(root)
        return minima
        