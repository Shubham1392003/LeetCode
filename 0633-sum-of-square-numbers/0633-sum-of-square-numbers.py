import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0                                  # this is left pionter left=0
        right = int(math.sqrt(c))                 # this is right pointer right=5 and math.sqrt will take squareroot(5)=2
        while left<=right:
            sumi=(left*left)+(right*right) # (0*0)+(2*2)=4
            if sumi == c:                  # 4==5 is not true
                return True
            elif sumi <= c:                 # 4<=5 is true 
                left+=1                     # so left will increase by one left=1 and right=2 and loop again
            else:
                right-=1 
        return False