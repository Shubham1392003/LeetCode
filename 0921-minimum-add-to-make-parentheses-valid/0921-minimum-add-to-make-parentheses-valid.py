class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        count = 0
       
        for ch in s:
            if ch == "(":
                st.append(ch)
            elif ch == ")":
                if len(st) > 0:
                    st.pop()
                else:
                    count+=1

        return count + len(st)


        