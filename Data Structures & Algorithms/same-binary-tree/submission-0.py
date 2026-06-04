# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        res_p = []
        res_q = []
        res = []

        def preorder(node):

            if node is None:
                res.append(None)
                return None
            
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        
        preorder(p)
        res_p = res
        res = []
        preorder(q)
        res_q = res

        # print(res_p)
        # print(res_q)
        return res_p == res_q
