'''
Created on 17/06/2014

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = filter(None, s.strip().split(" "))
        words = words[::-1]
        
        return " ".join(words)