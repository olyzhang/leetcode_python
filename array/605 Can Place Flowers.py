class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        is_pre_one = False
        max_places = 0
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 1:
                is_pre_one = True
            else:
                if is_pre_one:
                    is_pre_one = False
                else:
                    if i + 1 < length and flowerbed[i + 1] == 1:
                        i += 1
                        is_pre_one = True
                    else:
                        max_places += 1
                        if max_places == n:
                            return True
                        is_pre_one = True
            i += 1
        return False


if __name__ == "__main__":
    flowerbed = [0]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))
