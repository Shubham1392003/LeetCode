class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)
        count=0
        for ch in bit:
            if ch == "1":
                count +=1
        return count
        