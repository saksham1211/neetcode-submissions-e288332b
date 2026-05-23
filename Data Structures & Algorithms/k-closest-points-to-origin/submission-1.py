class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for x,y in points:
            d = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(minHeap, [d, [x, y]])



        while k>0:
            d, (x, y) = heapq.heappop(minHeap)
            res.append([x, y])
            k-=1

        return res