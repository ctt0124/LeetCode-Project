class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        

        s1 = s
        while(s1.find('()') > -1 or s1.find('[]') > -1 or s1.find('{}') > -1):
            s1 = s1.replace('()','')
            s1 = s1.replace('[]','')
            s1 = s1.replace('{}','')
        if(s1!=''):
            return False
        else:
            return True
