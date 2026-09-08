class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minmal = float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                minmal=min(minmal,abs(i-start))
        return minmal