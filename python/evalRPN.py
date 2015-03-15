'''
Created on 17/06/2014

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
# @param tokens, a list of string
# @return an integer
    def evalRPN(self, tokens):
        # Assumes valid input. Proper number of operands and integers,
        # and all tokens are either an integer or an operand
        values = []
        
        for t in tokens:
            if t == "+":
                values.append(values.pop() + values.pop())
            elif t == "-":
                b = values.pop()
                a = values.pop()
                values.append(a - b)
            elif t == "*":
                values.append(values.pop() * values.pop())
            elif t == "/":
                b = values.pop()
                #avoid zero division. Throw exception, but not in this test
                if b == 0:
                    pass
                a = values.pop()
                values.append(int(float(a) / b))
            else:
                values.append(int(t))
            
        #assert(len(values) == 1)
    
        return values.pop()