class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c:
            heapq.heappush(maxHeap, (-c, 'c'))

        res=""
        while maxHeap:
            cnt1, char1 = heapq.heappop(maxHeap)

            if len(res)>=2 and res[-1]==char1 and res[-2]==char1:
                if not maxHeap:
                    break
                cnt2, char2 = heapq.heappop(maxHeap)
                
                res+=char2
                cnt2+=1
                if cnt2!=0:
                    heapq.heappush(maxHeap, (cnt2, char2))
                heapq.heappush(maxHeap, (cnt1, char1))

            else:
                
                res+=char1
                cnt1+=1
                if cnt1!=0:
                    heapq.heappush(maxHeap, (cnt1, char1))

        return res