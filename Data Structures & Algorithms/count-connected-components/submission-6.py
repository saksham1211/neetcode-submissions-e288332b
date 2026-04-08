class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components=0
        adj=defaultdict(list)



        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visit=set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for child in adj[node]:
                dfs(child)

        for i in range(n):
            if i not in visit:
                components+=1
                dfs(i)

        return components



        


            