class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        res=0
        for a1, a2 in edges:
            adj[a1].append(a2)
            adj[a2].append(a1)

        visit=set()

        def dfs(node):
            visit.add(node)

            for i in adj[node]:
                if i not in visit:
                    dfs(i)

        for i in range(n):
            if i not in visit:
                dfs(i)
                res+=1

        return res