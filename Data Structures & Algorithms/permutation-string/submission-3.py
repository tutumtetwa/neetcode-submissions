class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            window = defaultdict(int)

            for c in s2[i : i + len(s1)]:
                window[c] += 1
            
            if window == count:
                return True
        return False