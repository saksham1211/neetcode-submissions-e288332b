class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)

        while maxHeap and len(maxHeap)>1:
            a, b = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            ans = abs(a-b)
            if ans > 0:
                heapq.heappush(maxHeap, -ans)

        return -maxHeap[0] if maxHeap else 0

            