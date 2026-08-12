class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # maxcount = 0
        # for i in range(len(nums)):
        #     freq = {}
        #     for j in range(i,len(nums)):
        #         freq[nums[j]]=freq.get(nums[j],0)+1
        #         key =max(freq, key=freq.get)
        #         count = freq[key]
        #         if count>k:
        #             break
        #         maxcount=max(maxcount,j-i+1)
        # return maxcount
        left = 0 
        maxcount=0
        freq={}
        for right in range(len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            maxcount=max(maxcount,right-left+1)
        return maxcount

