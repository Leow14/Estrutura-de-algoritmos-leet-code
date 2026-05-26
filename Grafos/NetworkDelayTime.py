import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}
        
        # Estrutura do times
        # [[2,1,1],[2,3,1]]
        # {2: {1: 1}} -> {2: {1: 1}, {3: 1}} 
        for items in times:

            if not graph.get(items[0]):
                graph[items[0]] = {items[1]: items[2]}
            else:
                graph[items[0]][items[1]] = items[2]

        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            distance, current_node = heapq.heappop(min_heap)

            if distance > distances[current_node]: 
                continue
            
            for neighbor, value in graph.get(current_node, {}).items():
                total_distance = distance + value
                if total_distance < distances[neighbor]: 
                    distances[neighbor] = total_distance
                    heapq.heappush(min_heap, (total_distance, neighbor))
                

        _max = -1
        if len(distances) > n:
            return _max
        
        for key, value in distances.items():
            _max = max(_max, value)

        if _max == float('inf'):
            return -1
        
        return _max



