# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def levelOrder(self, root):
        
        q = collections.deque()
        q.append(root)
        
        # [[3], [1, 4], [5]]
        res = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            if level:
                res.append(level)
        return res