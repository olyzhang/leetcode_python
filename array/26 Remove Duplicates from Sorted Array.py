class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n

        move_index = 1
        for i in range(1, n):
            if nums[i] > nums[move_index - 1]:
                nums[i], nums[move_index] = nums[move_index], nums[i]
                move_index += 1
        return move_index


if __name__ == "__main__":
    nums = [1, 2]
    print(Solution().removeDuplicates(nums))
    print(nums)
