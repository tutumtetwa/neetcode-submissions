class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) #[val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.hashmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        ans = ''
        # if key not in self.hashmap:
        #     return ans
        
        values = self.hashmap[key]
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        
        
