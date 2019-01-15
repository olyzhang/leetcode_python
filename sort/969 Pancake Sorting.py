class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        end = len(A) - 1
        for i in range(len(A), 0, -1):
            index = A.index(i)
            if index != i-1:
                A = A[:index + 1][::-1] + A[index + 1:]
                res.append(index+1)
                A = A[:end + 1][:: - 1] + A[end + 1:]
                res.append(i)
            end -= 1
        return res


if __name__ == '__main__':
    A = [3, 2, 4, 1]
    print(Solution().pancakeSort(A))
