class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Solution 1: time limit exceed
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, i + k + 1):
        #         if j >= n:
        #             break
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Solution 2
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


if __name__ == "__main__":
    nums = [99, 99]
    k = 2
    print(Solution().containsNearbyDuplicate(nums, k))
