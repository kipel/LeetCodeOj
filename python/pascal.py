'''
Created on 18/06/2014

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        '''
        Prints out n rows of Pascal's triangle.
        It returns False for failure and True for success.
        '''
        if numRows == 0:
            return []
    
        triangle = [[1]]
        
        for i in xrange(1, numRows):
            triangle.append([l+r for l,r in zip(triangle[i-1] + [0], [0] + triangle[i-1])])
    
        return triangle

''' 
Simple Testcases   
print generate(2)
print generate(4)
print generate(10)
print generate(1)
print generate(0)
'''