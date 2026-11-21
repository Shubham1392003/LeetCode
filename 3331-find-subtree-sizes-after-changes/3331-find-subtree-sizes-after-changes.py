class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        adj = [[] for _ in range(n)]

        for i in range(1, n):
            u = parent[i]
            v = i
            adj[u].append(v)

        resultSize = [1] * n
        last = [-1] * 26

        def dfs(currNode):
            c = ord(s[currNode]) - ord('a')

            nearestAncestor = last[c]

            last[c] = currNode

            for child in adj[currNode]:
                dfs(child)

            last[c] = nearestAncestor

            if currNode != 0:
                newParent = parent[currNode]

                if nearestAncestor != -1:
                    newParent = nearestAncestor

                parent[currNode] = newParent

                resultSize[newParent] += resultSize[currNode]

        dfs(0)

        return resultSize

        