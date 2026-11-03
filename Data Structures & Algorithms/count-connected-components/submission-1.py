class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        
        def dfs(i):
            seen.add(i)
            for nei in graph[i]:
                if nei not in seen:
                    dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        
        return ans