# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,res,node):
        if node is None:
            return
        self.inorder(res,node.left)
        res.append(node.val)
        self.inorder(res,node.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.inorder(res,root)
        return res
        