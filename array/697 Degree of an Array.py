class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = [1, i, i]
            else:
                num_dict[nums[i]][0] += 1
                num_dict[nums[i]][2] = i

        length, degree = 50001, 1
        for i in num_dict:
            # print(i, num_dict[i])
            if num_dict[i][0] > degree:
                length = num_dict[i][2] - num_dict[i][1] + 1
                degree = num_dict[i][0]
            elif num_dict[i][0] == degree:
                if num_dict[i][2] - num_dict[i][1] + 1 < length:
                    length = num_dict[i][2] - num_dict[i][1] + 1
        return length


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1]
    print(Solution().findShortestSubArray(nums))
