# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# # 时间/空间 复杂度 均为：O(N × N!)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, [], ans)
        
        return ans
    
    def dfs(self, subNums, path, ans):
        if not subNums:
            ans.append(path)
            return ans
        
        for i in range(len(subNums)):
            if i > 0 and subNums[i] == subNums[i-1]:
                continue
            self.dfs(subNums[:i]+subNums[i+1:], [subNums[i]]+path, ans)
