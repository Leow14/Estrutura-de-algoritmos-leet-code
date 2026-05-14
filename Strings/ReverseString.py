class Solution(object):
    def reverseOnlyLetters(self, s):
        arr = [ch for ch in s]
        left = 0
        right = len(s) - 1

        while left < right:

            if arr[left].isalpha() and arr[right].isalpha():
                arr[left], arr[right] = arr[right], arr[left]
                left    += 1
                right   -= 1
            
            elif arr[left].isalpha():
                right   -= 1
 
            elif arr[right].isalpha():
                left    += 1
            
            else:
                right   -= 1
                left    += 1

        return "".join(arr)





obj = Solution()
print(obj.reverseOnlyLetters("a1b2c3")) # output: c1b2a3
