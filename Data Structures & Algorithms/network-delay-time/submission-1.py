class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        ## dijiktras algorithm

        adj={i:[] for i in range(n+1)}

        for u, v, w in times:
            adj[u].append((w, v))

        minheap=[[0, k]]
        visit=set()
        res=0

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue

            res=w1
            visit.add(n1)
            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, [w1+w2, n2])

        return res if len(visit)==n else -1