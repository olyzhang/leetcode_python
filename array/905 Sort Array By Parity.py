class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_nums = []
        odd_nums = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_nums.append(A[i])
            else:
                odd_nums.append(A[i])
        return even_nums + odd_nums


if __name__ == "__main__":
    A = [2, 1, 2]
    print(Solution().sortArrayByParity(A))
