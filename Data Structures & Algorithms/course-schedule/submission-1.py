class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
        seen = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            
            if crs == []:
                return True
            
            seen.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            
            seen.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        