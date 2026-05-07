class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(nums):
            if len(nums) == 1:
                return [nums]
            perms = dfs(nums[1:])
            first = nums[0]
            # print(perms , first)

            res = []
            for p in perms:
                for i in range(len(p) + 1):
                    sub = p[:i] + [first] + p[i:]
                    # print(sub)
                    res.append(sub)
            return res
        return dfs(nums)

