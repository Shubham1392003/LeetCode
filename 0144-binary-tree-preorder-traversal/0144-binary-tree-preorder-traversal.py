# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preoder(self,res,node):
        if node is None:
            return
        res.append(node.val)
        self.preoder(res,node.left)
        self.preoder(res,node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.preoder(res,root)
        return res
        
        