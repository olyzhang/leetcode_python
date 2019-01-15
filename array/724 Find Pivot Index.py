class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0

        left_sum = 0
        right_sum = sum(nums[1:])
        if left_sum == right_sum:
            return 0
        for i in range(1, n):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1


if __name__ == "__main__":
    nums = [-1, -1, -1, 0, 1, 1]
    print(Solution().pivotIndex(nums))
