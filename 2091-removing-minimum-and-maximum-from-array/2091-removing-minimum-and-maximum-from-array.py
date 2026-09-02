class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        maxIdx =0
        minIdx =0
        for i in range(len(nums)):
            if nums[i]<nums[minIdx]:
                minIdx = i
            if nums[i]>nums[maxIdx]:
                maxIdx=i
        left = min(minIdx,maxIdx)
        right = max(maxIdx,minIdx)

        removeFront = right+1
        removeBack = len(nums)-left
        removeBoth = (left + 1)+(len(nums)-right)
        return min(removeBoth,min(removeBack,removeFront))