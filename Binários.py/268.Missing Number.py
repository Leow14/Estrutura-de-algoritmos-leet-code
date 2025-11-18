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

p = s.missingNumber([0, 1, 2, 4])

print(p)