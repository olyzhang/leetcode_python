class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        # if len(nums) <= 1:
        #     return nums

        # counts = [0, 0, 0]
        # length = len(nums)
        # for i in range(length):
        #     counts[nums[i]] += 1
        # for i in range(counts[0]):
        #     nums[i] = 0
        # for i in range(counts[0], counts[0] + counts[1]):
        #     nums[i] = 1
        # for i in range(counts[0] + counts[1], counts[0] + counts[1] + counts[2]):
        #     nums[i] = 2
        # return nums

        # Solution 2
        if len(nums) <= 1:
            return

        length = len(nums)
        zero_index = -1
        two_index = length
        i = 0
        while i < two_index:
            if nums[i] == 0:
                zero_index += 1 
                nums[i] = nums[zero_index]
                nums[zero_index] = 0
            elif nums[i] == 2:
                two_index -= 1
                nums[i] = nums[two_index]
                nums[two_index] = 2
                continue
            i += 1
        print(nums)


if __name__ == '__main__':
    nums = [1, 2, 0]
    print(Solution().sortColors(nums))
