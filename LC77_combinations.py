# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# You may return the answer in any order.
# Time complexity: O(k * Choose k from N)
# Space complexity: O(Choose k from N)



class Solution:
    def combine(self, n, k):
        ans = []
        
        def dfs(start, path, ans):
            if len(path) == k:
                ans.append(path)
                return
            
            # 比如 n = 100, k =20, 当path 取到 [1, 83]之后就不用继续了，因为后面还有84到100共17个数，无法得到一个 k= 20的结果了
            if (k - len(path)) > n + 1 - start:
                return
            
            for i in range(start, n+1):

                dfs(i+1, path+[i], ans)
                
        dfs(1, [], ans)
        
        return ans