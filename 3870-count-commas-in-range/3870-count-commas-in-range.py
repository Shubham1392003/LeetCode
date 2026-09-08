class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        # count=1
        # for i in range(1000,n):
        #     count +=1
        # return count
        ans = (n-1000)+1
        return ans
