class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0

        q=deque()
        while q or maxHeap:
            time+=1
            if maxHeap:
                currentTask = 1+heapq.heappop(maxHeap)
                if currentTask:
                    q.append((time+n, currentTask))

            if q and q[0][0]==time:
                _, currentTask = q.popleft()
                heapq.heappush(maxHeap, currentTask)

        return time