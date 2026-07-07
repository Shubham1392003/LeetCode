class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s=str(n)
        x=''
        sum=0
        for ch in s:
            if ch != '0':
                x+=ch
                sum+=int(ch)

        return int(x)*sum

        