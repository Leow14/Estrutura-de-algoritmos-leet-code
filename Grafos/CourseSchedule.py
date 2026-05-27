class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        
        # [0] -> Ainda não visitei
        # [1] -> Estou visitando
        # [2] -> Já visitei e não tem ciclo

        state = [0] * numCourses

        def has_cycle(num):
            if state[num] == 1:
                return True
            if state[num] == 2:
                return False
            
            state[num] = 1
            for neighbor in graph[num]:
                if has_cycle(neighbor):
                    return True
            
            state[num] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
            
        return True