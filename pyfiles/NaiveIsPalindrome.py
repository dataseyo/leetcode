class Solution(object):
    def isPalindrome(self, x):
        str1 = str(x)
        str2 = str1[::-1]
        #index1 = x[0]
        #index2 = len(x) - 1
        if str1 == str2:
            return True
        else: 
            return False
