class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # idx , height
        res = -1
        n = len(heights)
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                idx , height = stack.pop()
                area = (i - idx) * height
                start = idx
                res = max(res , area)
            stack.append((start , h))
        while stack:
            idx , height = stack.pop()
            area = ((n) - idx) * height
            res = max(res , area)
        # print(stack)
        return res