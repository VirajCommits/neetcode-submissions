class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        self.called = set()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value , timestamp))
        self.called.add(key)

    def get(self, key: str, timestamp: int) -> str:
        # print(self.cache , key)
        pos = ""
        for v , t in self.cache[key]:
            if timestamp == t:
                return v
            elif timestamp >= t:
                pos = v
        return pos
