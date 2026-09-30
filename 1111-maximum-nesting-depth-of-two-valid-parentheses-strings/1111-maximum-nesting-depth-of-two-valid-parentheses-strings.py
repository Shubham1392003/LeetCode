class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        result = []
        for i in range(len(seq)):
            if seq[i] == "(":
                depth+=1
                if depth%2==0:
                    result.append(1)
                else:
                    result.append(0)

            elif seq[i] == ')':
                if depth%2==0:
                    result.append(1)
                else: 
                    result.append(0) 
                depth-=1
        return result

        