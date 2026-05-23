class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.TweetMap = defaultdict(list)
        self.minHeap = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.TweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        maxHeap = []
        self.followMap[userId].add(userId)

        for follow in self.followMap[userId]:
            tweets  = self.TweetMap[follow]

            if tweets:
                index = len(tweets)-1
                time, tweetId = tweets[index]
                heapq.heappush(maxHeap, (-time, tweetId, follow, index-1))
        while maxHeap and len(res)<10:
            negTime, tweetId, follow, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            if index>=0:
                time, tweetId = self.TweetMap[follow][index]
                heapq.heappush(maxHeap, (-time, tweetId, follow, index-1))        
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)
        return
        
