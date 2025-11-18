def bit_count(list_nums):
        count = 1
        for num in list_nums:

            if num == 0:
                list_nums[num] = 0
            elif num == 1:
                list_nums[num] = 1
            elif is_power_of_2(num):
                power = num
                count = 1
                list_nums[num] = 1
            else:
                list_nums[num] = list_nums[power] + list_nums[count]
                count += 1
        return list_nums
         

def is_power_of_2(num):
    
    while num > 1:
        if num%2 == 0:
            num = num//2
        else:
            return False
    return True


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        return bit_count(list(range(n+1))) 
    

s = Solution()

a = s.countBits(128)
print(a)
