class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        if n == 1:
            return 0

        lead_zeros = 0
        is_lead_zeros = False
        end_zeros = 0
        max_zeros = 0
        cur_zeros = 0
        if seats[0] == 0:
            is_lead_zeros = True
        for i in range(n):
            if is_lead_zeros:
                if seats[i] == 0:
                    lead_zeros += 1
                    continue
                else:
                    is_lead_zeros = False
            if seats[i] == 0:
                cur_zeros += 1
            else:
                if cur_zeros > max_zeros:
                    max_zeros = cur_zeros
                cur_zeros = 0
        end_zeros = cur_zeros
        return max((max_zeros + 1) // 2, lead_zeros, end_zeros)


if __name__ == "__main__":
    seats = [0, 0, 0, 0]
    print(Solution().maxDistToClosest(seats))
