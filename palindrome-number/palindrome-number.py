class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        l = len(a)
        for i in range(0,l/2): 
            if(str(x)[i] != str(x)[l-1-i]):
                return False
        return True
            