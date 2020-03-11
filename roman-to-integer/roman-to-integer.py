class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,}
        dict2 ={'IV':4,
                'IX':9,
                'XL':40,
                'XC':90,
                'CD':400,
                'CM':900,}
        ret = 0

        for key in dict2.keys():
            if(key in s):
                print(key)
                ret = ret + dict2[key]
                s = s.replace(key,' ')
        for key in dict1.keys():
            if(key in s):
                ret = ret + s.count(key)*dict1[key]
                #ret = ret + dict1[key]
                s = s.replace(key,'')
        return ret
