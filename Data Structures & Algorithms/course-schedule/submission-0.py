class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        seen = set()
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(c):
            if c in seen:
                return False

            if c == []:
                return True
            
            seen.add(c)
            for pre in preMap[c]:
                if not dfs(pre):
                    return False

            seen.remove(c)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
