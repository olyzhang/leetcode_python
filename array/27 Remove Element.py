class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            if nums[i] == val:
                while res > i:
                    if nums[res - 1] != val:
                        nums[i] = nums[res - 1]
                        nums[res - 1] = val
                        res -= 1
                        break
                    res -= 1
        return res


if __name__ == "__main__":
    nums = [2, 2]
    val = 3
    print(Solution().removeElement(nums, val))
    print(nums)
