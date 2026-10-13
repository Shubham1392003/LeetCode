class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        temp =[]
        ans=0
        for num in nums:
            temp.append(num*num)
        temp.sort()
        k = len(nums)
        for i in range(k//2):
            ans-=temp[i]
        for i in range(k//2,k):
            ans+=temp[i]
        return ans
