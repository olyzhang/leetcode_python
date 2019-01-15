class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        length = len(S)
        if length < 3:
            return []
        left, right = 0, 0
        result = []
        while right < length:
            if S[right] == S[left]:
                right += 1
            else:
                if right - left >= 3:
                    result.append([left, right-1])
                left = right
        if right - left >= 3:
            result.append([left, right-1])
        return result


if __name__ == "__main__":
    s = "aaa"
    print(Solution().largeGroupPositions(s))
