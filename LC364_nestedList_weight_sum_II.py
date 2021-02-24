class Solution:
    def depthSumInverse(self, nestedList):
        
        # 和LC339 的思路基本一致，只是算depth时是逆的
        # 339最外层depth = 1，最内层depth = maxDepth
        # 此题， 最外层depth = maxDepth， 最内层depth = 1
        # 那么，depth_364 = maxDepth - depth_339 + 1
        # 只需要给每个integer 对应了depth_339之后，存放在res[]里，等待maxDepth得出之后，再进行sum运算即可
        # maxDepth 只需要和每一个depth比较，keep max值即可
        
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
        
