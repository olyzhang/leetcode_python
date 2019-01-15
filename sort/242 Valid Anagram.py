class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if len_s == 0 and len_t == 0:
            return True
        if len_s == 0 or len_t == 0:
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        return False


if __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'
    print(Solution().isAnagram(s, t))
