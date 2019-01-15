class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i == len(citations) - 1:
                if citations[i] > i:
                    result = i + 1
            else:
                if citations[i] > i:
                    result = i + 1
                else:
                    break
        return result

if __name__ == '__main__':
    citations = [100]
    print(Solution().hIndex(citations))
