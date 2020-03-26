class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while(True):
            try:
                print(i)
                if nums[i] == val:
                    del nums[i]
                else:
                    i = i+1
            except:
                break
        return len(nums)
