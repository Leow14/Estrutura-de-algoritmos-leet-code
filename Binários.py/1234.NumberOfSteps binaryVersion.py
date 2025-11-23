# Fazendo agora a mesma solução porém com operadores binários.

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            if num & 1 == 1:   # é ímpar
                num -= 1
            else:
                num >>= 1
            steps += 1

        return steps
