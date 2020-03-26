# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1==None and l2 == None):
            return None
        if(l2 == None):
            return l1
        if(l1 == None):
            return l2
        tmp = ListNode(0)
        ret = tmp
        tmp2 = ListNode(0)
        ll1 = l1
        ll2 = l2
        while(True):
            
            if(ll1.val <= ll2.val):
                tmp.val = ll1.val
                
                #tmp.next = ListNode(ll2.val)
                ll1 = ll1.next

            else:
                tmp.val = ll2.val

                #tmp.next = ListNode(ll1.val)
                ll2 = ll2.next
            if(ll1 == None) and (ll2 == None):
                break
            if(ll1 == None):
                tmp.next = ll2
                break
            if(ll2 == None):
                tmp.next = ll1
                break
            tmp.next = ListNode(0)
            tmp = tmp.next
           


        return ret
            
