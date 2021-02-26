# Time Complexity = O(n)
# Space Complexity = O(n)

def expand(s):
    ans = [""]
    stack = []
        
    i = 0
    option = 0
        
    while (i < len(s)):
        char = s[i]
        if char == '{':
            option = 1
        elif char == '}':
            option = 0
            ans = []
            while(len(stack)):
                ans += stack.pop()
        elif char != ',':
            if not option:
                ans = [token + char for token in ans]
            else:
                sub = [token + char for token in ans]
                stack.append(sub)
            
        i += 1
        
    ans.sort()   
    return ans

def main():
    expected = ["acdf","acef","bcdf","bcef"]

    print(expected == expand("{a,b}c{d,e}f"))

main()
