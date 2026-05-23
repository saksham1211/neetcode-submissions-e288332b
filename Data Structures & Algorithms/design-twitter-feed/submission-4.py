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
        tweets = []
        res = []
        tweets.extend(self.TweetMap[userId])
        for follow in self.followMap[userId]:
            tweets.extend(self.TweetMap[follow])

        heapq.heapify(tweets)
        while len(tweets)>10:
            heapq.heappop(tweets)

        maxHeap = [(-t, tw) for t, tw in tweets]

        heapq.heapify(maxHeap)
        while maxHeap:
            _, tw = heapq.heappop(maxHeap)
            res.append(tw)

        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)
        return
        
