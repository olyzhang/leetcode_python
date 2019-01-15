class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        result = set()
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        nums1.sort()
        nums2.sort()
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(result)


if __name__ == '__main__':
    nums1 = [1]
    nums2 = [1]
    print(Solution().intersection(nums1, nums2))
