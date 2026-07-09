class Solution:
    def countPrimes(self, n: int) -> int:
        # if n <= 2:
        #     return 0
        # count=0
        # for num in range(2,n):
        #     isPrime = True
        #     for i in range(2,int(num**0.5)+1):
        #         if num % i == 0:
        #             isPrime=False
        #             break
        #     if isPrime:
        #         count+=1
        # return count

        if n < 2:
            return 0
        a = [0 for  i in range(n)]
        a[0]=1
        a[1]=1

        for i in range(2,n):
            for j in range(i+i,n,i):
                a[j]=1
        count = 0
        for i in range(n):
            if a[i]==0:
                count+=1
        return count