class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num=start ^ goal
        count=0
        bits=bin(num)[2:]
        for ch in bits:
            if ch == '1':
                count+=1
        return count
        