'''
Created on 19/06/201

@author: Kippel @ ihaveseenthings.com
'''

def longestValidParentheses(s):
    lengths = []
    open_par = False
    


'''
Test cases
'''

print longestValidParentheses("(()")
print longestValidParentheses(")()())")
print longestValidParentheses("(((())))")
print longestValidParentheses("()()()()()")
print longestValidParentheses(")(()()(())()()")
print longestValidParentheses(")()()()(())()()(")
print longestValidParentheses(")()()()(())()()()()(")


'''
Only for pairs of parentheses: ()() not intelaced (())
    for p in s:
        if p == "(":
            if open_par:
                lengths.append(False)
            open_par = True
        elif p == ")":
            if open_par:
                lengths.append(True)
            else:
                lengths.append(False)
            open_par = False
    
    max_length = 0
    temp = 0
    for i in range(len(lengths)):
        if lengths[i]:
            temp += 2
        else:
            max_length = max(max_length, temp)
            temp = 0
    
    max_length = max(max_length, temp)
    return max_length
'''