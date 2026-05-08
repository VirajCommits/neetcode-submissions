class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open , close , cur):
            if open == close == n:
                res.append(cur)
                return
            if open == close:
                dfs(open + 1 , close , cur + "(")
            elif open == n:
                # close ones rem
                dfs(open , close + 1 , cur + ")")
            elif close == n:
                # open ones rem
                dfs(open + 1 , close , cur + "(")
            else:
                dfs(open + 1 , close , cur + "(")
                dfs(open , close + 1 , cur + ")")


        dfs(0 , 0 , "")
        return res