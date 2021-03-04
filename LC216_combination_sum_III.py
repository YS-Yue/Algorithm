# Time Complexity: O(K * 2^K)
# Time Complexity: O(K)

class Solution:
    def combinationSum3(self, k: int, n: int):
        available = [i for i in range(1, 10)]
        ans = []
        self.dfs(k, available, n, [], ans)
        return ans
        
        
    def dfs(self, k, available, target, path, ans):
        
        if target == 0 and len(path) == k:
            ans.append(path)
            return
        
        if len(path) == k or target < 0:
            return
        
        for i in range(len(available)): 
            if available[i] > target:
                return
            self.dfs(k, available[i+1:], target - available[i], path + [available[i]], ans)