class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time=0
        q=deque()

        while maxheap or q:
            time+=1

            if maxheap:
                currenttask=1+heapq.heappop(maxheap)

                if currenttask:
                    q.append((time+n, currenttask))

            if q and q[0][0]==time:
                _, taskcount=q.popleft()
                heapq.heappush(maxheap, taskcount)

        return time