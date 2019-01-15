class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1
        res = []
        n = len(nums)
        if n <= 1:
            return res
        for i in range(n):
            if nums[i] < 0:
                continue
            num = nums[i]
            nums[i] = 0
            while True:
                if nums[num - 1] < 0:
                    res.append(num)
                    break
                elif nums[num - 1] == 0:
                    nums[num - 1] = -1
                    break
                else:
                    tmp = nums[num - 1]
                    nums[num - 1] = -1
                    num = tmp
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDuplicates(nums))
