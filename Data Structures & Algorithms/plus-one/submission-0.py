class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        s = ''
        for d in digits:
            s += str(d)
        
        num = int(s) + 1
        print(num)
        s = str(num)
        for d in s:
            ans.append(d)
        
        print(ans)

        return ans