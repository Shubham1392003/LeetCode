class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # ans = 0
        # l,r=0,len(nums)-1
        # while l<=r:
        #     if nums[r]>=nums[l] and nums[r]<=x:
        #         x=x-nums[r]
        #         ans+=1
        #         r-=1
        #     elif nums[l]>=nums[r] and nums[l]<=x:
        #         x=x-nums[l]
        #         ans+=1
        #         l+=1
        #     elif x==0:
        #         return ans
    
        # if x!=0:
        #     return -1

        target = sum(nums)-x
        if target < 0:
            return -1
        max_len=-1
        curr_sum=0
        l=0

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum > target and l <= r:
                curr_sum -= nums[l]
                l+=1

            if curr_sum == target:
                max_len =max(max_len,r-l+1)
        return -1 if max_len == -1 else len(nums)-max_len

        