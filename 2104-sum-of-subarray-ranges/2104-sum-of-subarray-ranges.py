class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            small=nums[i]
            large=nums[i]
            for j in range(i,n):
                small = min(small,nums[j])
                large = max(large,nums[j])
                total += (large - small)
        return total

        