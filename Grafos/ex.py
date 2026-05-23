from typing import Optional
from collections import deque



# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []




class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        q = deque([node])
        clones = {}
        clones[node] = Node(node.val, [])

        while q:
            curr = q.popleft()
            clone_curr = clones[curr]

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                clone_curr.neighbors.append(clones[neighbor])
            
        return clones[node]
