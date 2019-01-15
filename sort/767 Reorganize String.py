import collections


class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        len_S = len(S)
        if len_S <= 1:
            return S

        count = collections.Counter(S)
        digit0 = max(count.keys(), key=lambda x: count[x])

        an = [digit0] * count[digit0]
        i = 0
        for digit in count:
            if digit != digit0:
                for _ in range(count[digit]):
                    an[i % len(an)] += digit
                    i += 1
        return ''.join(an) if i >= len(an) - 1 else ''


if __name__ == '__main__':
    S = "aaabb"
    print(Solution().reorganizeString(S))
