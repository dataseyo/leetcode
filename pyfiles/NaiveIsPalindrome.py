class Solution(object):
    def isPalindrome(self, x):
        str1 = str(x) # change int to string
        str2 = str1[::-1] # reverse string
        #index1 = x[0]
        #index2 = len(x) - 1
        if str1 == str2: # compare strings
            return True
        else: 
            return False
