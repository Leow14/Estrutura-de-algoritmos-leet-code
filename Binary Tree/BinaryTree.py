class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

# Funções para inserir dados/nodos dentro da árvore

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

    def dfs(self, val):
        return self._dfs_recursive(self.root, val)

    def _dfs_recursive(self, node, val):

        if node is None:
            return False

        print(node.val)
        if node.val == val:
            return True
        if self._dfs_recursive(node.left, val):
            return True
        if self._dfs_recursive(node.right, val):
            return True
        return False


# Funções de transversals recursivas
    # Funções preorder
    def preorder_transversal(self):
        result = []

        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    # Funções inorder

    def inorder_transversal(self):
        result = []

        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    # Funções postorder

    def postorder_transversal(self):
        result = []

        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)


tree = BinaryTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18, 20]
for val in values_to_insert:
    tree.insert(val)

print(tree.dfs(40))
#print(tree.search(14))
#print(tree.search(10))
#print(tree.search(18))

print(f'preorder: {tree.inorder_transversal()}')
