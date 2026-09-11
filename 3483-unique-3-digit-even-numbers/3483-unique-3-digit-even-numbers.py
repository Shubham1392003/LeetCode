class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = 0
        wish  = [False]*1000
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == j or i == k or digits[k]%2 != 0:
                        continue
                    x = digits[i]*100 + digits[j]*10 + digits[k]
                    if not wish[x]:
                        wish[x]=True
                        ans+=1
        return ans

