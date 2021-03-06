# Better than 96.34% runtime and 96.93% memory usage.
# Time complexity = Space complexity: O(3^N * 4^M), where N is the number of the digits in the input that maps to 3 letters, and M is the number of digits in the input that maps to 4 letters, and N+M is total number digits in the input.
class Solution:
    def letterCombinations(self, digits):
        dic = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r","s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
              }
        if len(digits) == 0:
            return []
        digit_list = list(digits)
        res = []
        
        def dfs(index, path, res):
            if index == len(digit_list):
                res.append(path)
                return
            sub = []
            for v in dic[digit_list[index]]:
                for p in path:
                    sub.append( p + v )
            path = sub
            dfs(index+1, path, res)
            
        dfs(0, [""], res)
        return res[0]
            