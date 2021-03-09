# Better than 99.35% runtime and 88.72% memory usage
# Time complexity : O(N*2^N)
# Space complexity : O(N*2^N) characters stored in the return list. 
class Solution:
    def generateAbbreviations(self, word):
        
        res = ["1", word[0]]
        
        for i in range(1, len(word)):
            letter = word[i]
            
            update = []
            for r in res:
                update.append(r+letter)
                
                lastC = r[-1]
                if lastC.isdigit():
                    update.append(r[:-1]+str(1+int(lastC)))
                else:
                    update.append(r+"1")
            
            res = update.copy()
            
        return res
            