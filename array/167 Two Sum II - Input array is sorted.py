class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = 0, len(numbers) - 1
        while index1 != index2:
            total = numbers[index1] + numbers[index2]
            if total == target:
                break
            elif total < target:
                index1 += 1
            else:
                index2 -= 1
        return [index1 + 1, index2 + 1]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
