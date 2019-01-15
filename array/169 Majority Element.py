class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] in d:
        #         d[nums[i]] += 1
        #     else:
        #         d[nums[i]] = 1
        #     if d[nums[i]] >= len(nums) / 2:
        #             return nums[i]

        # Solution: O(n)
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
                count = 1
            elif nums[i] == major:
                count += 1
            else:
                count -= 1
        return major


if __name__ == "__main__":
    nums = [3]
    print(Solution().majorityElement(nums))
