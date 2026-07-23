class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        total = 0
        leftmax = 0
        rightmax = 0

        left = 0
        right = n-1

        while left < right:
            if height[left]<=height[right]:
                #left side 
                if leftmax > height[left]:
                    total += leftmax - height[left]
                else:
                    leftmax = height[left]
                left+=1
            else:
                #right side
                if rightmax > height[right]:
                    total += rightmax - height[right]
                else:
                    rightmax = height[right]
                right-=1
        return total
