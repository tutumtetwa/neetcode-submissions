class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        maxh = [-cnt for cnt in count.values()]
        time = 0
        heapq.heapify(maxh)

        while q or maxh:
            time += 1

            if maxh:
                cnt = 1 + heapq.heappop(maxh)
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxh, q.popleft()[0])
        return time