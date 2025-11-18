class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        bit_n = bin(n)[2:]
        count = 0
        for i in bit_n:
            if i == '1':
                count += 1

        return count
    


