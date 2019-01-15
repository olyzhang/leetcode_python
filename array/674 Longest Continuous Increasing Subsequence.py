class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        max_len = 1
        cur_len = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1
        return max(cur_len, max_len)


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    print(Solution().findLengthOfLCIS(nums))
