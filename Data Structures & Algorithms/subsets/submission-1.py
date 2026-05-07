class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i , curList):
            # print(i , curList)
            if curList not in ans:
                ans.append(curList)

            if i >= len(nums):
                return []
            # choose i
            newList = curList.copy()
            newList.append(nums[i])
            dfs(i + 1 , newList)
            # dont choose i
            dfs(i + 1 , curList)
        dfs(0 , [])
        return ans
