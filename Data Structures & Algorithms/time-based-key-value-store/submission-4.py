class TimeMap:

    def __init__(self):
        self._l1_pair = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._l1_pair:
            self._l1_pair[key] = []
            self._l1_pair[key].append([timestamp, value])
            return
        self._l1_pair[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self._l1_pair:
            return ""
        l, r = 0, len(self._l1_pair[key])-1
        ret = ""
        while l <= r:
            m = (r+l)//2
            if self._l1_pair[key][m][0] <= timestamp:
                l = m+1
                ret = self._l1_pair[key][m][1]
            else:
                r = m-1
        return ret