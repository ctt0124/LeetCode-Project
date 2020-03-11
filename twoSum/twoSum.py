class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in range(0,len(nums)):
            try:
                id2 = nums.index(target - nums[i],i+1)
                print(id2)
            
                ret.append(i)
                ret.append(id2)
                break
            except:
                pass
        return ret
                
            