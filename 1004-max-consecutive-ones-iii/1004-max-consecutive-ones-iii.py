class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxlen=0
        # for i in range(len(nums)):
        #     zeros=0
        #     for j in range(i,len(nums)):
        #         if nums[j]==0:
        #             zeros+=1
        #         if zeros<=k:
        #             currlen=j-i+1
        #             maxlen=max(currlen,maxlen)
        #         else:
        #             break
        # return maxlen

        n=len(nums)
        l,r=0,0
        zeros,maxlen=0,0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros > k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros <=k:
                length = r-l+1
                maxlen=max(maxlen,length)
            r+=1
        return maxlen
        