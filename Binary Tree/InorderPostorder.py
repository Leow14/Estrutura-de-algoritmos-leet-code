# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        # inorder = [9, 3, 15, 20, 7]
        # postorder = [9, 15, 7, 20, 3]

        if postorder and inorder:
            root = TreeNode(postorder.pop())
            root_index = inorder.index(root.val)

            root.right = self.buildTree(inorder[root_index+1:], postorder)

            root.left = self.buildTree(inorder[:root_index], postorder)

            return root
        return None
