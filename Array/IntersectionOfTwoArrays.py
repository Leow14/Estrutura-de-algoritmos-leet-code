class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        result = []

        for num in set_nums1:
            if num in set_nums2:
                if num not in result:
                    result.append(num)
        return result