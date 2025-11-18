class Solution(object):
    def countBits(self, n):
        
        bin_list = [x for x in range(n + 1)]
        power = 1
        for number in bin_list[2:]:
            if power * 2 == number:
                power = number
            bin_list[number] = 1 + bin_list[number - power]

        return bin_list
        # dp[n - num if is_power_of_2(num)]

s = Solution()

a = s.countBits(8)
print(a)
