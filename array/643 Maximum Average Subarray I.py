class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n == k:
            return sum(nums) / k

        max_total = 0
        cur_total = 0
        for i in range(k):
            cur_total += nums[i]
        max_total = cur_total
        for i in range(k, n):
            cur_total += nums[i] - nums[i-k]
            if max_total < cur_total:
                max_total = cur_total
        return max_total / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6]
    k = 4
    print(Solution().findMaxAverage(nums, k))
