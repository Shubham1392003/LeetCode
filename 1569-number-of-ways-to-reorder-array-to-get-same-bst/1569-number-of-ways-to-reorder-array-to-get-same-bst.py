class Solution:
    MOD = 1_000_000_007

    def solve(self, nums, PT):
        m = len(nums)

        if m < 3:
            return 1

        root = nums[0]
        left = []
        right = []

        for i in range(1, m):
            if nums[i] < root:
                left.append(nums[i])
            else:
                right.append(nums[i])

        left_ways = self.solve(left, PT) % self.MOD
        right_ways = self.solve(right, PT) % self.MOD

        return (
            left_ways * right_ways % self.MOD
            * PT[m - 1][len(left)]
        ) % self.MOD

    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)

        PT = [[1] * (i + 1) for i in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, i):
                PT[i][j] = (
                    PT[i - 1][j - 1] + PT[i - 1][j]
                ) % self.MOD

        return (self.solve(nums, PT) - 1) % self.MOD