# Faster than 98.87% runtime, less than 80.80% memory usage.
# Time complexity / Space complexity: O(N * 2^N)
class Solution:
    def subsets(self, nums):

        res = [[]]
        
        for n in nums:
            sub = []
            
            for r in res:
                sub.append(r+[n])
            
            res += sub.copy()
            
        return res