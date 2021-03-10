# Time Complextiy: O(1), 因为最多跑8个起始数，每个跑8次while循环
# Space Complexity: O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int):
        res = []
        
        def helper(startDigit):
            num, endDigit = startDigit, startDigit
            while num < low and endDigit <= 9:
                endDigit += 1
                num = num * 10 + endDigit
            
            while num <= high and endDigit <= 9:
                res.append(num)
                endDigit += 1
                num = num * 10 + endDigit
                
        for i in range(1, 9):
            helper(i)
            
        res.sort()   
        return res