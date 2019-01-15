class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur_index = 0
        for i in range(length):
            if nums[i] != 0:
                nums[cur_index] = nums[i]
                cur_index += 1
        for i in range(cur_index, length):
            nums[i] = 0
        return nums


if __name__ == "__main__":
    nums = [0, 1, 0]
    print(Solution().moveZeroes(nums))
