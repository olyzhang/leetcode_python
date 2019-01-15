class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(len(A)-2):
            j, k = i+1, i+2
            if A[i] < A[k] + A[j]:
                return A[k] + A[j] + A[i]
        return 0


if __name__ == "__main__":
    A = [3, 6, 2, 3]
    print(Solution().largestPerimeter(A))
