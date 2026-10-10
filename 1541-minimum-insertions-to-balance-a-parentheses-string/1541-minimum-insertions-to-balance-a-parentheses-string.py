class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        res = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                count += 1
            else:
                if count > 0:
                    count -= 1

                    if i + 1 < n:
                        if s[i + 1] == ')':
                            i += 1
                        else:
                            res += 1
                    else:
                        res += 1
                else:
                    if i + 1 < n:
                        if s[i + 1] == ')':
                            res += 1
                            i += 1
                        else:
                            res += 2
                    else:
                        res += 2

            i += 1

        res += count * 2
        return res
                

        