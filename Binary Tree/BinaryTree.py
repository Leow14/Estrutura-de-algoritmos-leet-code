class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_recursive(val, self.root)

    def _insert_recursive(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_recursive(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_recursive(val, node.right)

    def search(self, val):
        return self._search_recursive(self.root, val)
  
    def _search_recursive(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)


tree = BinaryTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for val in values_to_insert:
    tree.insert(val)

print(tree.search(7))
print(tree.search(14))
print(tree.search(10))
print(tree.search(18))
