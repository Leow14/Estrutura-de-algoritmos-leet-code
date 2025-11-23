class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2:
                num -= 1
                num /= 2
            steps += 1
    
        return steps