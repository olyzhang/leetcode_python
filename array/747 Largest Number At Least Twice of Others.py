class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            max_num = nums[0]
            next_num = nums[1]
            index = 0
        else:
            max_num = nums[1]
            next_num = nums[0]
            index = 1
        for i in range(2, n):
            if nums[i] > max_num:
                next_num = max_num
                max_num = nums[i]
                index = i
            elif nums[i] > next_num:
                next_num = nums[i]
        if max_num >= 2 * next_num:
            return index
        else:
            return -1
        return index


if __name__ == "__main__":
    nums = [0, 0, 3, 2]
    print(Solution().dominantIndex(nums))
