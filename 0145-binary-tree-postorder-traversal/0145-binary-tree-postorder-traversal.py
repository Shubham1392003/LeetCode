# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,res,node):
        if node is None:
            return
        self.postorder(res,node.left)
        self.postorder(res,node.right)
        res.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.postorder(res,root)
        return res
        