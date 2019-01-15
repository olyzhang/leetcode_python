class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 1
        length = len(A)
        if length <= 2:
            return False
        while i < length:
            if A[i] == A[i-1]:
                return False
            if A[i] < A[i-1]:
                break
            i = i + 1
        if i == 1:
            return False
        while i < length:
            if A[i] > A[i-1] or A[i] == A[i-1]:
                return False
            i += 1
            if i == length:
                return True
        return False


if __name__ == "__main__":
    A = [0,3,2,1]
    print(Solution().validMountainArray(A))
