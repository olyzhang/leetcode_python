class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        beg, end = -1, -2
        min_num, max_num = nums[n - 1], nums[0]
        for i in range(1, n):
            max_num = max(nums[i], max_num)
            min_num = min(nums[n-i-1], min_num)
            if nums[i] < max_num:
                end = i
            if nums[n - i - 1] > min_num:
                beg = n - i - 1
        return end - beg + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(nums))
