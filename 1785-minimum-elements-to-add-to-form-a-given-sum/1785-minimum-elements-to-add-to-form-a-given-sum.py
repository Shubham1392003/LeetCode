class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        # sum_num=0
        # for num in nums:
        #     sum_num+=num
        # res=abs(goal - sum_num)
        # count=0
        # while res>0:
        #     res-=limit
        #     count+=1
        # return count

        total = sum(nums)
        res = abs(goal-total)
        return (res+limit-1)//limit
        
        