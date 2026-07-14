class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        i=0
        while i < n-1:
            if arr[i]>=arr[i+1]:
                break
            i+=1
        if i==0 or i==n-1:
            return False
        while i<n-1:
            if arr[i]<=arr[i+1]:
                return False
            i+=1
        return True

        