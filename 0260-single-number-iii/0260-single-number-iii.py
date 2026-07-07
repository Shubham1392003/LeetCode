class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n=len(nums)
        xor = 0
        for num in nums:
            xor ^= num
        
        rightmost = xor & -xor
        xor1,xor2=0,0
        for i in range(n):
            if nums[i] & rightmost:
                xor1 ^= nums[i]
            else:
                xor2 ^= nums[i]

        return [xor1,xor2]