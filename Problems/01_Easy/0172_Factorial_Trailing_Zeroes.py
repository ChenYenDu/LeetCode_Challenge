class Solution:
    def trailingZeroes(self, n: int) -> int:
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot
