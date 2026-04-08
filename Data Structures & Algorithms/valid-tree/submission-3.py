class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visit=set()
        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for child in adj[node]:
                if child==prev:
                    continue

                if not dfs(child, node):
                    return False

            return True

        return dfs(0, -1) and len(visit)==n
 
            
