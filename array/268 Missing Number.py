class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # n = len(nums)
        # sum = n * (n + 1) / 2
        # for i in range(n):
        #     sum -= nums[i]
        # return int(sum)

        # Solution 2: XOR operator, a ^ b ^ b = a
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(Solution().missingNumber(nums))
