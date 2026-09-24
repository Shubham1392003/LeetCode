class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = 0
        i=0
        for x in nums:
            digit = 0
            while x>0:
                x,r=divmod(x,10)
                digit += r
            if digit == i:
                return i
            i+=1
        return -1

                    

            
        