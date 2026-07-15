import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0                                  # this is left pionter left=0
        right = int(math.sqrt(c))                 # this is right pointer right=5
        while left<=right:
            sumi=(left*left)+(right*right) # (0*0)+(5*5)=25
            if sumi == c:                  # 25==5 is not true
                return True
            elif sumi <= c:                 # 25<=5 is not true 
                left+=1
            else:
                right-=1 # so right will move 5 to 4 and again this loop will excute for left=0 and right=4
        return False