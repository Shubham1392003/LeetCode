class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        mid = n//2

        st = [''] * n

        st[:mid] = sorted(s[:mid])

        if n % 2 == 1:
            st[mid] = s[mid]
        
        for i in range(mid):
            st[n-1-i]=st[i]
            
        return "".join(st)
        