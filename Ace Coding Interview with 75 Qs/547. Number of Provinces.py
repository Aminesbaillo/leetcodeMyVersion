class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
         
        def dfs(node, visited):
            visited.add(node)
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor, visited)
        n = len(isConnected)
        visited = set()
        province = 0
        
        for i in range(n):
            if i not in visited:
                province += 1
                dfs(i, visited)
        return province 
        
sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
