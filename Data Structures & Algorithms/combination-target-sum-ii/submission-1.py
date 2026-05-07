class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return 1
        n = len(candidates)
        candidates.sort()
        res = []
        cur = []
        def dfs(i , total):
            # print(cur)
            if total == target:
                if cur not in res:
                    res.append(cur.copy())
                return
            if total > target or i >= n:
                return
            cur.append(candidates[i])
            dfs(i + 1 , total + candidates[i])
            cur.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1 , total)
        dfs(0 , 0)
        return res
