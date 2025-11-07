class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        counter = {}
        lo = 0
        hi = 0

        while hi < len(nums):
            
            if nums[hi] in counter:
                return True
            else:
                counter[nums[hi]] = 1  # não existe duplicata, então adiciona no dicionário
                
            if hi - lo >= k:
                del counter[nums[lo]] # andamos com o dicionário, então remova esse chave \ valor do dicionário
                lo += 1
            hi += 1
         
        return False

s = Solution()

print(s.containsNearbyDuplicate([1,2,3,1], 3))  # esperado: True
print(s.containsNearbyDuplicate([1,0,1,1], 1))  # esperado: True
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # esperado: False