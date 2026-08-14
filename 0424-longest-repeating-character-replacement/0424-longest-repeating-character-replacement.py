class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maxlen = 0
        # for i in range(len(s)):
        #     hash = [0]*26
        #     maxfq=0
        #     for j in range(i,len(s)):
        #         hash[ord(s[j])-ord('A')]+=1
        #         maxfq = max(maxfq,hash[ord(s[j])-ord('A')])
        #         change = (j-i+1)-maxfq
        #         if change<=k:
        #             maxlen=max(maxlen,j-i+1)
        #         else:
        #             break
        # return maxlen

        maxlen=0
        maxfq = 0
        l,r=0,0
        hash=[0]*26
        while r < len(s):
            hash[ord(s[r])-ord('A')]+=1
            maxfq = max(maxfq,hash[ord(s[r])-ord('A')])
            if (r-l+1)-maxfq > k:
                hash[ord(s[l])-ord('A')]-=1
                l+=1
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen