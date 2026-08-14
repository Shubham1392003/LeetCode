class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq ={}
        length =0
        l,r=0,0
        while r<len(s):
            freq[s[r]]=freq.get(s[r],0)+1
            while freq[s[r]] > 2:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            length = max(length,r-l+1)
            r+=1
        return length     