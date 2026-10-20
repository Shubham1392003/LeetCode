class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)
        result = [1]

        if n != 1:
            result.append(n)

        y = 2
        while y <= n // 2:
            if n % y == 0:
                result.append(y)
            y += 1

        temp = sorted(nums)

        if temp == nums:
            return sum(result)

        for k in result:
            valid = True
            prevMax = -1

            for start in range(0, n, k):
                drop = 0

                for j in range(start, start + k - 1):
                    if nums[j] > nums[j + 1]:
                        drop += 1

                if nums[start + k - 1] > nums[start]:
                    drop += 1

                if drop > 1:
                    valid = False
                    break

                mn = nums[start]
                mx = nums[start]

                for j in range(start, start + k):
                    mn = min(mn, nums[j])
                    mx = max(mx, nums[j])

                if start > 0 and prevMax > mn:
                    valid = False
                    break

                prevMax = mx

            if valid:
                total += k

        return total
        


        
        
        
