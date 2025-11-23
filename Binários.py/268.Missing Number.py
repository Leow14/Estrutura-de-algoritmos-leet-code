class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution = 0
        x = 1
        for num in nums:
            solution ^= num
            solution ^= x
            x += 1
        return solution
    

s = Solution()

p = s.missingNumber([0, 1, 2, 3, 4, 5, 7, 8, 9])

print(p)