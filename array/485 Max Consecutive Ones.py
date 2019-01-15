class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
            else:
                cur_len = 0
            if cur_len > max_len:
                max_len = cur_len
        return max_len


if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
