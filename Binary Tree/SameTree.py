import collections


class Solution(object):
    def isSameTree(self, p, q):

        if q is None and p is None:
            return True
        elif q is None or p is None:
            return False

        queue = collections.deque()
        queue.append(p)

        queue2 = collections.deque()
        queue2.append(q)

        while queue and queue2:
            node = queue.popleft()
            node2 = queue2.popleft()

            if not (node.val == node2.val):
                return False

            if (node.left is None) != (node2.left is None):
                return False

            if (node.right is None) != (node2.right is None):
                return False

            if node.left and node2.left:
                queue.append(node.left)
                queue2.append(node2.left)

            if node.right and node2.right:
                queue.append(node.right)
                queue2.append(node2.right)

        return True
