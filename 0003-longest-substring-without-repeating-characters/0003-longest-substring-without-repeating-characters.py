class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #BRUTE FORCE O(N*2) AND SPACE O(256) of hash_set
        # n=len(s)
        # maxval = 0
        # for i in range(n):
        #     hash_set = [0]*256
        #     for j in range(i,n):
        #         if hash_set[ord(s[j])]==1:
        #             break
        #         hash_set[ord(s[j])]=1
        #         currle=j-i+1
        #         maxval = max(maxval,currle)
        # return maxval

        #OPTIMAL SOLUTION 
        n=len(s)
        hash=[-1]*256
        l,r,maxlen=0,0,0
        while r<n:
            if hash[ord(s[r])]!=-1:
                l=max(hash[ord(s[r])]+1,l)
            currlen=r-l+1
            maxlen=max(maxlen,currlen)
            hash[ord(s[r])]=r
            r+=1
        return maxlen
        