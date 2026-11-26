class Solution:
    def canAliceWin(self, n: int) -> bool:
        def can(n, m):
            n -= m

            if n < 0:
                return False

            if m == 1:
                return True

            return not can(n, m - 1)

        return can(n, 10)
        