class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap , -1 * s)
        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            res = abs(a - b)
            heapq.heappush(maxHeap , -1 * res)
        return -1 * maxHeap[0]