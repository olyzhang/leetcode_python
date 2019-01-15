class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # Solution 1
        # if len(bits) == 0:
        #     return False

        # is_one = False
        # i = 0
        # while i < len(bits):
        #     if bits[i] == 0:
        #         i += 1
        #         is_one = True
        #     else:
        #         i += 2
        #         is_one = False
        # return is_one

        # Solution 2
        ones = 0
        i = len(bits) - 2
        while i >= 0:
            if bits[i] == 1:
                ones += 1
            else:
                break
            i -= 1
        if ones % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    bits = [1, 0, 1, 0]
    print(Solution().isOneBitCharacter(bits))
