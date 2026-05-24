class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []

        for i, (enqTime, processTime) in enumerate(tasks):
            heapq.heappush(pending, (enqTime, processTime, i))

        time = 0
        res=[]
        while pending or available:
            while pending and pending[0][0]<=time:
                enqTime, pTime, i = heapq.heappop(pending)
                heapq.heappush(available, (pTime, i))

            if not available:
                time = pending[0][0]
                continue

            processTime, i = heapq.heappop(available)
            time+=processTime
            res.append(i)


        return res