class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    nums = [-1, 0, 1, 4, 3, 2]
    print(Solution().arrayPairSum(nums))
