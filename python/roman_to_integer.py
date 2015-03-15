'''
Created on 18/06/201

@author: Kippel @ ihaveseenthings.com
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        single_letter= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        double_letter= {"IV":4, "IX": 9, "XL":40, "XC":90, "CD":400, "CM":900}
    
        roman = s.upper()
        i, number = 0, 0
        while i < len(roman):
            if roman[i:i+2] in double_letter:
                number += double_letter[roman[i:i+2]]
                i += 2
            else:
                number += single_letter[roman[i]]
                i += 1
    
        return number