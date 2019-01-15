class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Solution 1: just do as the problem state: reverse each line
        # and toggle each value
        # if len(A) == 0:
        #     return A

        # for list in A:
        #     length = len(list)
        #     if length == 0:
        #         continue
        #     for i in range(length//2):
        #         tmp = list[i]
        #         list[i] = list[length-i-1]
        #         list[length-i-1] = tmp
        #     for i in range(length):
        #         list[i] = 1 - list[i]
        # return A

        # Solution 2: one line solution
        # row[::-1] will get a reverse row
        return [[1 ^ i for i in row[::-1]] for row in A]


if __name__ == "__main__":
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(Solution().flipAndInvertImage(A))
