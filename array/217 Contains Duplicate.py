class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False

        distinct = set()
        for i in range(len(nums)):
            if nums[i] in distinct:
                return True
            else:
                distinct.add(nums[i])
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]
    print(Solution().containsDuplicate(nums))
