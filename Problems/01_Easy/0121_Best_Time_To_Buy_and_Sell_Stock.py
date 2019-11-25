class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        dp = [0] * len(prices)
        for i in range(len(prices)):
            dp[i] = max(dp[i-1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]


'''
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
                return 0
            minPrice = prices[0]
            maxProfit = 0
            for p in prices:
                if p < minPrice:  # pass p to minPrice if it's smaller 
                    minPrice = p
                elif p - minPrice > maxProfit: # when found p > minPrice and larger than maxProfit pass it
                    maxProfit = p - minPrice
            return maxProfit

    
'''
