# 时间复杂度： O（S），其中S为所有可行解的长度之和， 比较松的上界为指数级别的O（n * 2^n），实际并不会达到。
# 空间复杂度：O（target），除答案数组外，空间负责度取决于递归栈的深度， 在最差情况下需要递归 O（target）层（比如candidates中有1）
# Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.
# Time Complexity: O(N ^ (T/M + 1))
# Space Complexity: O(T/M)

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], ans)
        return ans
        
    def dfs(self, candidates, startIndex, target, path, ans):
        if target == 0:
            ans.append(path)
            return
        
        for i in range(startIndex, len(candidates)):
            # i 只有在 cadidates[i]不能继续重复使用的情况下，进入下一个loop（即i+=1）
            if target < candidates[i]:
                return
            # 只要还有重复使用的可能，就call下一层，i不变，target减一次，path里加上。
            self.dfs(candidates, i, target - candidates[i], path +[candidates[i]], ans)
            