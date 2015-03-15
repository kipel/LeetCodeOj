'''
Created on 18/06/201

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        values = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC",
                  50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V",  4:"IV", 1:"I"}
        n = num
        roman = ""
    
        keys = sorted(values.keys())[::-1]
        for k in keys:
            while n >= k:
                roman = roman + values.get(k)
                n -= k
    
        return roman
'''
Test cases
print intToRoman(3999)
print intToRoman(3000)
print intToRoman(2999)
print intToRoman(999)
print intToRoman(349)
print intToRoman(9)
print intToRoman(1)
print intToRoman(2014)
'''