class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        for i in range(len(s)):
            mapS[s[i]] += 1
            mapT[t[i]] += 1
        
        for key in mapS:
            if mapS[key] != mapT[key]:
                return False
        
        return True
