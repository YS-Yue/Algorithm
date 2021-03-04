# Time Complexity: O((2^n)
# Space Complexity: O(N) #最多会call N层stack

class Solution:
    def combinationSum2(self, candidates):
        ans = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], ans)
        return ans
    
    def dfs(self, candidates, startIndex, target, path, ans):

        if target == 0:
            ans.append(path)
            return
            
        for i in range(startIndex, len(candidates)):
            if candidates[i] > target:
                return
            
            # 例如candidates中有10 个 2， 第一个2 call dfs 递归的时候已经将会用到的所有2都用过了，所以从第二个2作为startIndex已经不需要再重复递归了
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, i+1, target - candidates[i], path + [candidates[i]], ans)
        