class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        counter = {}

        for num in nums:
            if counter.get(num):
                return True
            counter[num] = 1
        return False