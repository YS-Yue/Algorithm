#本题需要特别注意copy的使用的必要性（注：slice [:] 和.copy() 相同）
# 时间/空间 复杂度 均为：O(N × N!)

class Solution:
    def permute(self, nums):
        self.ans = []
        self.nums = nums
        visited = [0] * len(nums)
        self.dfs([], visited)
        
        return self.ans
        

    def dfs(self, subNums, visited):
        if sum(visited) == len(visited):
            self.ans.append(subNums.copy())
            return
            
        else:
            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    subNums.append(self.nums[i])
                    self.dfs(subNums, visited)
                    visited[i] = 0
                    subNums.pop()
                        
   
    def permute2(self, nums):
        res = []

        def helper(vals, cands):
            if len(vals) == len(nums):
                res.append(vals)
                return
            for i in range(len(cands)):
                helper(vals + [cands[i]], cands[:i] + cands[i+1:])
                
        helper([], nums)
        return res 


    def permute3(self, nums):
        if len(nums) == 1:
            return [nums]
        
        ans = []
        
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            
            rest_permutation = self.permute(rest)
            
            for p in rest_permutation:
                ans.append([nums[i]] + p)
                
        return ans
       