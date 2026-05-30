class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        print(results)

        # results      =    [ 0,  0,  0,  0,  0,  0]
        # temperatures =    [73, 74, 71, 72, 75, 72]
        # output       =    [1 ,  3,  1,  1, -1, -1]

        current_temp = temperatures[0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                stack_index = stack.pop()
                result_index = i - stack_index
                results[stack_index] = result_index
            stack.append(i)
        return results