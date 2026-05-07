class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        cur = []
        res = []
        def dfs(i):
            if i >= n:
                if cur not in res:
                    res.append(cur.copy())
                return
            
            # choose i
            cur.append(nums[i])
            # if cur not in res:
            # res.append(cur.copy())
            dfs(i + 1)
            cur.pop()
            # if cur not in res:
            # res.append(cur.copy())
            dfs(i + 1)
            # print(res)
        dfs(0)
        return res