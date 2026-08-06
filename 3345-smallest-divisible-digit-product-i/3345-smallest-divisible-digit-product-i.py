class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # current = n
        # while True:
        #     product = 1
        #     temp = current
        #     while temp>0:
        #         digit = temp%10
        #         product *= digit 
        #         temp //=10
        #     if  product % t==0:
        #         return current
        #     else:
        #         current +=1

        while True: 
            product =1
            for digit in str(n):
                product *= int(digit)
            if product % t == 0:
                return n
            n+=1
        