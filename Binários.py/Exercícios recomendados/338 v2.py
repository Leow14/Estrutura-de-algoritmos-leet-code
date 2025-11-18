def is_power_of_2(num):
    
    while num > 1:
        if num%2 == 0:
            num = num//2
        else:
            return False
    return num


class Solution(object):
    def countBits(self, n):
        
        bin_list = [x for x in range(n + 1)]
        power = 0
        for number in bin_list[2:]:
            if is_power_of_2(number):
                power = number
                bin_list[number] = 1            
            else:
                bin_list[number] = 1 + bin_list[number - power]

        return bin_list
        # dp[n - num if is_power_of_2(num)]

s = Solution()

a = s.countBits(128)
print(a)
