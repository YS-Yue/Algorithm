# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
#
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum_DFS(self, nestedList):
        
        def dfs(nestedList, depth):
            totalSum = 0
            for element in nestedList:
                if element.isInteger():
                    totalSum += element.getInteger() * depth
                else:
                    totalSum += dfs(element.getList(), depth+1)
            
            return totalSum
        
        return dfs(nestedList, 1)


    def depthSum_BFS(self, nestedList):
        
        #bfs
        totalSum = 0
        stack = []
        stack.append([nestedList, 1])
        
        while(len(stack)):
            nestedCurrent, depth = stack.pop()
            for ele in nestedCurrent:
                if ele.isInteger():
                    totalSum += ele.getInteger() * depth
                else:
                    stack.append([ele.getList(), depth+1])
        
        return totalSum