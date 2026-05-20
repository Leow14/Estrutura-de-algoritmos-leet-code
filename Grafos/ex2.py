
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node):
        if not node: return None

        clones = {}
        clones[node] = Node(node.val, [])

        q = deque([node])

        while q:
            curr = q.popleft()
            curr_clone = clones[curr]

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)

                curr_clone.neighbors.append(clones[neighbor])

        return clones[node]