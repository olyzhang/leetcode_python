class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_nums = []
        odd_nums = []
        result = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_nums.append(A[i])
            else:
                odd_nums.append(A[i])
        for i in range(len(even_nums)):
            result.append(even_nums[i])
            result.append(odd_nums[i])
        return result


if __name__ == "__main__":
    A = [4,5,2,7]
    print(Solution().sortArrayByParityII(A))
