class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        res=""
        cnt1 = cnt2= 0
        char1=char2=""
        while maxHeap:
            

            if maxHeap:
                cnt1, char1 = heapq.heappop(maxHeap)

                if maxHeap:
                    cnt2, char2 = heapq.heappop(maxHeap)

                else:
                    cnt2 = 0
                    char2=""
            else:
                cnt1=0
                char1=""
            
            res+=char1
            res+=char2
            cnt1+=1
            cnt2+=1
            
            if cnt1<0:
                heapq.heappush(maxHeap, (cnt1, char1))

            if cnt2<0:
                heapq.heappush(maxHeap, (cnt2, char2))

            if len(res)>=2 and res[-1]==res[-2]:
                return ""
        return res               
