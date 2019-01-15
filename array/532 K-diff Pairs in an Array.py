class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n <= 1 or k < 0:
            return 0

        num_count = {}
        res = 0
        for i in nums:
            num_count[i] = num_count.setdefault(i, 0) + 1
        for key, value in num_count.items():
            if k == 0:
                if value >= 2:
                    res += 1
            else:
                if key + k in num_count.keys():
                    res += 1
        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 1
    print(Solution().findPairs(nums, k))
