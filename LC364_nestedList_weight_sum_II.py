class Solution:

        # 和LC339 的思路基本一致，只是算depth时是逆的
        # 339最外层depth = 1，最内层depth = maxDepth
        # 此题， 最外层depth = maxDepth， 最内层depth = 1
        # 那么，depth_364 = maxDepth - depth_339 + 1
        # 只需要给每个integer 对应了depth_339之后，存放在res[]里，等待maxDepth得出之后，再进行sum运算即可
        # maxDepth 只需要和每一个depth比较，keep max值即可
        # 线性时间复杂度，Time Complexity = O(N + K), N = integer 个数， K为层数
    def depthSumInverse_BFS(self, nestedList):
        self.maxDepth = 1
        res = []
        
        stack = [[nestedList, 1]]

        while (len(stack)):
            nestCurrent, depth = stack.pop()
            self.maxDepth = max(self.maxDepth, depth)
            for nest in nestCurrent:
                if nest.isInteger():
                    res.append([nest.getInteger(), depth])
                else:
                    stack.append([nest.getList(), depth+1])
        
        return sum((v*(self.maxDepth - d + 1)) for v, d in res)
     

      #dfs 的方法
    # Time complexity = O(N + M)  N = number of integers, M = depth/stacks
    # Space complexity = O(N + M) 
    def depthSumInverse_DFS(self, nestedList):
        self.totalSum = 0
        
        def dfs(nestedList):
            if len(nestedList) == 0:
                return 1
            nextLevelList = []
            currentSum = 0
            for ele in nestedList:
                if ele.isInteger():
                    currentSum += ele.getInteger()
                else:
                    nextLevelList += ele.getList()
            depth = dfs(nextLevelList)
            self.totalSum += currentSum * depth
            
            return depth + 1
        
        dfs(nestedList)
        return self.totalSum  
