class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for idx, num in enumerate(nums):
            if num in d:
                return d[num], idx
            d[target - num] = idx


s = Solution()

print(s.twoSum([2, 9, 13, 14], 15)) # esperado : 0, 2
print(s.twoSum([2, 9, 3, 7], 10)) # esperado :2, 3
print(s.twoSum([45, 2, 7, 1], 3)) # esperado : 1, 3
print(s.twoSum([5, 4, 1, 1], 2)) # esperado : 2, 3 