class TimeMap:

    def __init__(self):
        self._l1_pair = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._l1_pair:
            self._l1_pair[key] = {}
            self._l1_pair[key][timestamp] = value
            return
        self._l1_pair[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in self._l1_pair:
            return ""
        if timestamp in self._l1_pair[key]:
            return self._l1_pair[key][timestamp]
        timestamp_int = timestamp
        print(self._l1_pair)
        while timestamp_int >= 0:
            if timestamp_int in self._l1_pair[key]:
                return self._l1_pair[key][timestamp_int]
            timestamp_int -= 1
        return ""
        
