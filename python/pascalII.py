'''
Created on 18/06/2014

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row = [1] 
        n = 1
        #The judger counts rows starting from 0
        # 1st row is [1, 1] and not [1]
        for col in range(1, rowIndex+1):
            n = n * (rowIndex+1 - col) / col
            row.append(n)    

        return row