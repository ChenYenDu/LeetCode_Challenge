class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

    """
    [1,2,3,4,5]
    i = 1, total = 1 
    i = 2, total = 2
    i = 3, total = 3
    i = 4, total = 4
    """
