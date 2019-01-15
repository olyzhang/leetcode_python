class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <= 1:
            return True

        n = len(nums)
        is_modified = False
        for i in range(n - 1):
            if (nums[i] > nums[i + 1]):
                if is_modified:
                    return False
                else:
                    if i > 0:
                        if nums[i + 1] >= nums[i - 1]:
                            nums[i] = nums[i - 1]
                        else:
                            nums[i + 1] = nums[i]
                    else:
                        nums[i] = nums[i + 1]
                    is_modified = True
        return True


if __name__ == "__main__":
    nums = [2, 3, 3, 2, 4]
    print(Solution().checkPossibility(nums))
