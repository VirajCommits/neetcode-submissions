class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                idx , val = stack[-1]
                res[idx] = abs(idx - i)
                stack.pop()
            stack.append((i , t))

        return res