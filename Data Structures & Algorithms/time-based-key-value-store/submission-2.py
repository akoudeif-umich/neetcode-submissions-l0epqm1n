"""
set stores the key with a value at the give time stamp

get returns the most recent value of the key if key exists
and the most recent time stamp (prev time) is less than passed in time

how do I keep track of the most recent time_stamp 
"""

class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store key : value at time stamp
        # maybe map 
        self.time[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        best = ""
        if key in self.time:
            for vals in self.time[key]:
                if vals[1] <= timestamp:
                    best = vals[0]
        return best
        
