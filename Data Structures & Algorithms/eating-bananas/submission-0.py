class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPos(piles , target):
            res = 0
            for pile in piles:
                    if pile % target != 0:
                        res += (pile // target) + 1
                    else:
                        res += (pile // target)
            print(target , res)
            return res <= h
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            # print("TRYING:",mid)
            if isPos(piles, mid):
                print("worked:",mid)
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res if res != 0 else 1