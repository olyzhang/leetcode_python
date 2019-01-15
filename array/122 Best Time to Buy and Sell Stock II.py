class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Solution 1
        # if len(prices) == 0:
        #     return 0

        # min = prices[0]
        # max = min
        # profit = 0
        # for i in range(1, len(prices)):
        #     # print(min, max)
        #     if prices[i] >= max:
        #         max = prices[i]
        #     else:
        #         profit += max - min
        #         min = prices[i]
        #         max = min
        # profit += max - min
        # return profit

        # Solution 2
        profit = 0
        for i in range(len(prices) - 1):
            if (prices[i + 1] > prices[i]):
                profit += prices[i + 1] - prices[i]
        return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
