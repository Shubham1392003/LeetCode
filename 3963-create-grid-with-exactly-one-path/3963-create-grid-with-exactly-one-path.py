class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        for i in range(m):
            string =''
            for j in range(n):
                if i == 0:
                    string += '.'
                    continue
                if j == n-1:
                    string += '.'
                    continue
                string += '#'
            ans.append(string)
        return ans
                    

        