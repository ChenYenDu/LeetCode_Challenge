class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP O(n) time, O(1) space
        # ik: max include house k
        # ek: max exclude house k, (Note: ek is also the maximum for house 1,...,k-1)
        # i[k+1]: num[k] + ek # can't include house k
        # e[k+1]: max(ik, ek) # can either include house k or exclude house k
        i, e = 0, 0
        for n in nums: # from k-1 to k
            i, e = n+e, max(i, e)
        return max(i, e)
