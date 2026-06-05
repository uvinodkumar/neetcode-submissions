# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([])

        queue.append(root)

        result = []

        if root is None:
            return []

        while len(queue) != 0:

            level = []

            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result


