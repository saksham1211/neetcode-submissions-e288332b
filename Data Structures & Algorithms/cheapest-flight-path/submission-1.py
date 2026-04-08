class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        
        # Priority queue -> (cost, current node, stops)
        pq = [(0, src, 0)]
        
        # Best cost to reach each node with a certain number of stops
        best = {}
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            # If we reached the destination
            if node == dst:
                return cost
            
            # If we exceed the number of stops, continue
            if stops > k:
                continue
            
            # If this path offers a cheaper way to reach `node` with `stops`
            if (node, stops) in best and best[(node, stops)] <= cost:
                continue
            best[(node, stops)] = cost
            
            # Add all the neighbors to the queue
            for neighbor, price in adj[node]:
                heapq.heappush(pq, (cost + price, neighbor, stops + 1))
        
        return -1