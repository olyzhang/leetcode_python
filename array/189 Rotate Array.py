class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        n = len(nums)
        rotate_times = k % n
        if n <= 1 or rotate_times == 0:
            return
        nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 6
    Solution().rotate(nums, k)
    print(nums)
