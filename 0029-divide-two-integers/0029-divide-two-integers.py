class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        ans = 0
        n = abs(dividend)
        d = abs(divisor)
        while(n>=d):
            count=0
            while(n>=(d<<(count+1))):
                count+=1
            ans+=(1<<count)
            n-=d*(1<<count)

        ans *= sign
        return min(max(-2**31,ans),2**31 - 1)
        