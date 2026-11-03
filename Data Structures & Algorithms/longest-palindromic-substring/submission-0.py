class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans =''
        longestword = 0

        for i in range(len(s)):

            #odd lenght
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longestword:
                    ans = s[l : r + 1]
                    longestword = r - l + 1
                l -= 1
                r += 1

            #even length
            l = i
            r = i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longestword:
                    ans = s[l : r + 1]
                    longestword = r - l + 1
                l -= 1
                r += 1
        return ans
        