'''
Created on 16/06/2014

@author: Kippel
'''

def isInterleave(s1, s2, s3):
    '''
        Find all the characters of s1 and s2 in s3, and remove
        them from s3. If s3 is a combination of s1 and s2 the
        final string must be of length zero.
        
        Also, if the lenght of s3 doesn't equal the sum of the
        lengths of s1 and s2 we know it is not a combination.
        And, if after removing all characters of s1 found in s3,
        the length is different than s2, we know that there is
        at least one character that it is not in s1 or s2.
    '''
    
    len_s2 = len(s2)
    s = s3
    


    if len(s) != 0:
        return False
    
    return True

print isInterleave("aabcc", "dbbca", "aadbbcbcac")
print isInterleave("aabcc", "dbbca", "aadbbbaccc")