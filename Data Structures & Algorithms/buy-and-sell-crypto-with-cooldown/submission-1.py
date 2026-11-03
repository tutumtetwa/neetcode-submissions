class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #if buying: i + 1
        #if selling: i + 2
        dp = {} # (i, buying(T or F)) -> amount(max_profit)

        def dfs(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)

            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)

            return dp[(i, buying)]
        
        return dfs(0, True)
        