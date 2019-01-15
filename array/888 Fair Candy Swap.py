class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if int(diff + b) in A:
                return (int(diff + b), b)


if __name__ == "__main__":
    A = [1, 2, 5]
    B = [2, 4]
    print(Solution().fairCandySwap(A, B))
