class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        slide_window = set()
        for i in range(len(nums)):
            if nums[i] in slide_window:
                return True
            slide_window.add(nums[i])
            if len(slide_window)>k:
                slide_window.remove(nums[i-k])
        return False
        