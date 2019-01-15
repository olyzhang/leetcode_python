class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candyCrush(self, board):
        # Write your code here
        return 0


if __name__ == '__main__':
    board = [[110, 5, 112, 113, 114], [
                210, 211, 5, 213, 214], [
                310, 311, 3, 313, 314], [
                410, 411, 412, 5, 414], [
                5, 1, 512, 3, 3], [
                610, 4, 1, 613, 614], [
                710, 1, 2, 713, 714], [
                810, 1, 2, 1, 1], [
                1, 1, 2, 2, 2], [
                4, 1, 4, 4, 1014]]
    print(Solution().candyCrush(board))
