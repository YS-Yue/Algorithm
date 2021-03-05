# Time Complexity: O(2^n)
# Space Complexity: O(log n)

class Solution:
    def getFactors(self, n):
        res = []
        self.dfs(n, 2, [], res)
        return res
        
    def dfs(self, n, start, sub, res):
        while start * start <= n:
            if n % start == 0:
                res.append(sub + [start, n//start])
                self.dfs(n//start, start, sub + [start], res)
            start += 1
