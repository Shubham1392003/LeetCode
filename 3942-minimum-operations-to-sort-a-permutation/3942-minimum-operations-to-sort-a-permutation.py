class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ase_count = 0
        des_count = 0
        for i in range(1,n):
            ase_count += (nums[i]==(nums[i-1]+1)%n)
            des_count += (nums[i-1]==(nums[i]+1)%n)

        if ase_count == n-1 and nums[0]==0:
            return 0
        
        if ase_count==n-1:
            left_rot = n-nums[0]
            right_rot = 1+(nums[-1]+1)+1
            return min(left_rot,right_rot)
        
        if des_count==n-1:
            left_rot = n-nums[-1] + 1
            right_rot = (nums[0]+1)%n + 1
            return min(left_rot,right_rot)

        return -1