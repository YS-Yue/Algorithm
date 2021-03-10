# Time complexity: O(N * 2^N)
# Space complexity: O(N * 2^N)

class Solution:
    def letterCasePermutation(self, S):
        res = [""]
        
        for c in S:
            update = []
            for r in res:
                if c.isdigit():
                    update.append(r+c)
                else:
                    update.append(r+c.upper())
                    update.append(r+c.lower())
            res = update.copy()
            
        return res