class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewStr = ""

        for c in s:
            if c.isalnum():
                NewStr += c.lower()
        return NewStr == NewStr[::-1]
        

        