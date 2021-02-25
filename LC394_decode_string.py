# 使用stack存储当前状态，再进入下一级
# 每一级结束后，pop（）可逐层返回当时的状态
# Time complexity = O(n)
# Space complexity - O(n)

def decodeString(s):
    stack = []
    cur_token = ""
    next_times = "0"

    for char in s:
        if char.isdigit():
            next_times += char
        elif char.isalpha():
            cur_token += char
        elif char == "[":
            stack.append([cur_token, next_times])
            cur_token = ""
            next_times = "0"
        elif char == "]":
            pre_token, cur_times = stack.pop()
            cur_token = pre_token + cur_token*(int(cur_times))
    
    return cur_token

def main():
    print(decodeString("2[abc]3[cd]ef"))
    print(decodeString("abc3[cd]xyz"))
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))


main()

