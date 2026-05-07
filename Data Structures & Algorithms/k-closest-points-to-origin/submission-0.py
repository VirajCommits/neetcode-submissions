class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def find(x1 , y1 , x2 , y2):
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        minHeap = []
        for x , y in points:
            dist = find(0 , 0 , x , y)
            # print(dist)
            heapq.heappush(minHeap , (dist , (x , y) ))
        res = []
        while k > 0:
            _ , (x , y) = heapq.heappop(minHeap)
            res.append((x , y))
            k -= 1
        return res