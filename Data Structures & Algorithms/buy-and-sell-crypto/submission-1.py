class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r
        
        return ans