class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, node, result):
        self._inorder(node.left, result) + [node.value] + self._inorder(node.right, result)
