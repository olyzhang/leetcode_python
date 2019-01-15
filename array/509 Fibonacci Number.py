class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
        #      4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        # return F[N]
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)

if __name__ == "__main__":
    N = 30
    print(Solution().fib(30))
