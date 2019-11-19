class Solution1:
    '''
    記憶化搜尋：把歷遍的答案記下避免重複計算產生超時問題
    '''

    def __init__(self):
        self.memo = dict()  # create a empty dictiony to save result
        self.memo[0] = 1  # stage = 0  step = 1
        self.memo[1] = 1  # stage = 1  step = 1

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        steps = self.climbStairs(n-1)+self.climbStairs(n-2)
        self.memo[n] = steps
        return steps


class Solution2:
    '''
    動態規劃: 建立一個數組, 從頭開始歷遍, 這題的答案是前2個數相加, 看最後一個數值就好

    '''

    def ClimbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


class Solution3:
    '''
    空間壓縮： 觀察可得所由解答可由 stage = 1 跟 stage = 2 取得進行改寫
    '''

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
