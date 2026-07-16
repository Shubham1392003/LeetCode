# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root,maxi):
        if root is None:
            return 0
        lh = max(0,self.height(root.left,maxi)) # why max() is used here we avoiding the negative value if height give any negative value it will return ( 0 )
        rh = max(0,self.height(root.right,maxi))
        maxi[0]=max(maxi[0],lh+rh+root.val)
        return root.val + max(lh,rh)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[float('-inf')]
        self.height(root,maxi)
        return maxi[0]
        