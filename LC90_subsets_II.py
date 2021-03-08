# Time complexity / Space complexity: O(N * 2^N)
class Solution:
    def subsetsWithDup(self, nums):
        
        def dfs(nums, path):
            res.append(path)
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                
                dfs(nums[i+1:], path + [nums[i]])
        
        nums.sort()
        res = []
        dfs(nums, [])
        return res
            