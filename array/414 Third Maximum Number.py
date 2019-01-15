class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [float('-inf'), float('-inf'), float('-inf')]
        for i in nums:
            if i not in v:
                if i > v[0]:
                    v = [i, v[0], v[1]]
                elif i > v[1]:
                    v = [v[0], i, v[1]]
                elif i > v[2]:
                    v = [v[0], v[1], i]
        return v[2] if float('-inf') not in v else v[0]


if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    print(Solution().thirdMax(nums))
