class Twitter:

    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followmap[userId].add(userId)
        res = []
        maxHeap = []

        for followee in self.followmap[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1

                count, tweetId = self.tweets[followee][index]
                heapq.heappush(maxHeap, [count, tweetId, followee, index - 1])

        while maxHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(maxHeap, [count, tweetId, followee, index - 1])
        
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

        
