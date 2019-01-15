class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        for i in range(1, len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (
                i % 2 == 1 and nums[i] < nums[i - 1]
            ):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)
