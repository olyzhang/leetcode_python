class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Solution 1
        # isInc = True
        # isDec = True
        # for i in range(len(A)-1):
        #     isInc &= A[i] <= A[i+1]
        #     isDec &= A[i] >= A[id+1]
        # return isInc or isDec

        # Solution 2
        return len({x < y for x, y in zip(A, A[1:]) if x != y}) <= 1


if __name__ == "__main__":
    A = [2, 1, 2]
    print(Solution().isMonotonic(A))
