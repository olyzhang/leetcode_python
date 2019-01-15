class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        is_plus = 1
        for i in range(n - 1, -1, -1):
            digits[i] += is_plus
            if digits[i] == 10:
                is_plus = 1
                digits[i] = 0
            else:
                is_plus = 0
                break
        if is_plus == 1:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    digits = [8, 9]
    print(Solution().plusOne(digits))
