class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev = 1  # f(n-2)
        cur = 1   # f(n-1)
        # 費氏數列： f(n) = f(n-1)+f(n-2)
        for i in range(2, n+1):
            temp = cur   # f(n-1)
            cur = cur + prev  # calcuate f(n)
            prev = temp   # f(n-1) will become f(n-2) at the next iteration
        return cur  
