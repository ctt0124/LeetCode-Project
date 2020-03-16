class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str2 = strs[1::]
        ret = ''
        if(strs == []):
            return ret
        elif(len(strs) == 1):
            return strs[0]
        else:
            for i in range(0,len(strs[0])):
                for j in range(1,len(strs)):
                    if(len(strs[j]) - i > 0):
                        print('%s,%s'%(strs[0][i],strs[j][i]))
                        if(strs[0][i] != strs[j][i]):
                            ret = strs[j][0:i]
                            return ret
                    else:
                        ret = strs[j]
                        return ret
        return strs[0]
