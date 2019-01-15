class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        if length == 0:
            return []

        # Solution 1: time limit exceeded
        # res = [0] * length
        # rows = len(updates)
        # if rows == 0:
        #     return res
        # for [left, right, inc] in updates:
        #     for i in range(left, right + 1):
        #         if i >= length:
        #             break
        #         res[i] += inc
        # return res

        # Solution 2
        res = [0] * length
        rows = len(updates)
        if rows == 0:
            return res
        add = [0] * (length + 1)
        for [left, right, inc] in updates:
            add[left] += inc
            add[right + 1] -= inc
        for i in range(length):
            res[i] = add[i] + res[i - 1]
        return res


if __name__ == '__main__':
    length = 5
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
        ]
    print(Solution().getModifiedArray(length, updates))
