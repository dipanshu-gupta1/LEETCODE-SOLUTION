class Solution:
    def canAliceWin(self, n: int) -> bool:
        req = 10
        moves = 0

        while n >= req:
            n -= req
            req -= 1
            moves += 1

        return moves % 2 == 1