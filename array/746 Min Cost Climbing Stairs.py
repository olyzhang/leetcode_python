class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        return min(dp[n-1], dp[n-2])


if __name__ == "__main__":
    cost = [10, 15, 20]
    print(Solution().minCostClimbingStairs(cost))
