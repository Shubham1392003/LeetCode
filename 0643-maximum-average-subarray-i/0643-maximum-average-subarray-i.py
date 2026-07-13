class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum =0
        ans=0
        for i in range(k):
            window_sum+=nums[i]
        ans = window_sum / k
        for right in range(k,len(nums)):
            window_sum+=nums[right]-nums[right-k]
            ans=max(ans,window_sum/k)
        return ans
    
        