class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        min = prices[0]
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                if prices[i + 1] < min:
                    min = prices[i + 1]
            else:
                if profit < prices[i + 1] - min:
                    profit = prices[i + 1] - min
        return profit


if __name__ == "__main__":
    prices = [7, 5, 4, 3, 5]
    print(Solution().maxProfit(prices))
