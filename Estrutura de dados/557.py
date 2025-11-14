class Solution(object):
    def reverseWords(self, s):
        answer = ''
        l, r = 0, 0
        
        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                answer += s[l:r+1][::-1]
                r += 1
                l = r
        answer += ' '
        answer += s[l:r + 2][::-1]
        return answer[1:]

result = Solution().reverseWords("leonardo amorim de araujo")
print(result)