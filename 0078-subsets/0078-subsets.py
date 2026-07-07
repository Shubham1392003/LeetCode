class Solution:
    # def func(self,ind,lists,ans,nums,n):
    #     if ind == n:
    #         ans.append(lists[:])
    #         return
    #     self.func(ind+1,lists,ans,nums,n)
    #     lists.append(nums[ind])
    #     self.func(ind+1,lists,ans,nums,n)
    #     lists.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans=[]
        # lists=[]
        # self.func(0,lists,ans,nums,len(nums))
        # return ans

        n = len(nums)
        ans=[]
        count=2**n
        for val in range(count):
            subset=[]
            for i in range(n):
                if val & 2**i:
                    subset.append(nums[i])
            ans.append(subset)
        return ans

        