class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x>=0):
            ret = int(str(x)[::-1],10)
        else:
            ret = 0 - int(str(x)[1::][::-1],10)
        print(ret)
        print((1<<31-1))
        if(((0-(1<<31))>= ret) or (((1<<31)-1)<= ret)):
            return 0
        else:
            return ret