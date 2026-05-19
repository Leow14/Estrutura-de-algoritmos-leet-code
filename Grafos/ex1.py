from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        q = deque([node])

        clones = {}
        clones[node.val] = Node(node.val, [])
        while q:
            curr = q.popleft()
            curr_clone = clones[curr.val]

            for n in curr.neighbors:
                if n.val not in clones: # O(1)
                    clones[n.val] = Node(n.val, [])
                    q.append(n)

                curr_clone.neighbors.append(clones[n.val])

        return clones[node.val]