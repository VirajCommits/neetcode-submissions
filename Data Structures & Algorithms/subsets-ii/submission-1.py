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
            dfs(i + 1)
            cur.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i + 1)
        dfs(0)
        return res