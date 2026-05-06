class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a , b = nums1 , nums2
        if len(b) > len(a):
            a , b = b , a
        tot = len(a) + len(b)
        half = tot // 2
        l , r = 0 , len(b) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            a_l = a[j] if j >= 0 else float("-inf")
            a_r = a[j + 1] if j + 1 < len(a) else float("inf")
            b_l = b[i] if i >= 0 else float("-inf")
            b_r = b[i + 1] if i + 1 < len(b) else float("inf")
            # print(a_l , a_r , b_l , b_r , a , b)
            if a_l <= b_r and b_l <= a_r:
                if tot % 2:
                    return min(a_r , b_r)
                else:
                    return (max(a_l , b_l) + min(a_r , b_r)) / 2
            if b_l < a_r:
                l = i + 1
            else:
                r = i - 1
        
        return -1