class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Solution 1
        # if not nums:
        #     return 0

        # n = len(nums)
        # for i in range(n):
        #     if target <= nums[i]:
        #         return i
        # return n

        # Solution 2
        if not nums:
            return 0

        if target > nums[len(nums) - 1]:
            return len(nums)

        left = 0
        right = len(nums) - 1
        mid = 0
        while right > left:
            mid = (left + right) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur > target:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    nums = [1]
    target = 2
    print(Solution().searchInsert(nums, target))
