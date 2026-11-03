"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x : x.start)
        minheap = [] #end times

        for inter in intervals:
            if minheap and minheap[0] <= inter.start:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap, inter.end)
        
        return len(minheap)