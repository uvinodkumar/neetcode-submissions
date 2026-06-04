# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = deque([])

        queue.append(root)
        
        if root is None:
            return []

        while len(queue) != 0:
            level = []
            size = len(queue)

            for _ in range(size):
                e = queue.popleft()
                level.append(e.val)
            
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)

            res.append(level)

        return res
