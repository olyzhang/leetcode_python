class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if len(s) == 0 or len(d) == 0:
            return ""

        result = ""
        max = 0
        len_s = len(s)
        for t in d:
            len_t = len(t)
            i = j = 0
            while i < len_s and j < len_t:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len_t:
                if max < len_t:
                    result = t
                    max = len_t
                elif max == len_t:
                    for i in range(max):
                        if result[i] == t[i]:
                            continue
                        elif result[i] > t[i]:
                            result = t
                        break
        return result


if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    d = ["word", "good", "best", "good"]
    print(Solution().findLongestWord(s, d))
