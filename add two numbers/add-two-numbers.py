# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ''
        s2 = ''
        node = l1
        
        while(node):
            s1 = str(node.val) + s1
            print(s1)
            node = node.next
        node = l2
        while(node):
            s2 = str(node.val) + s2
            node = node.next
        sum = int(s1,10)+int(s2,10)
        sum = list(str(sum))

        
        r1 = ListNode(sum[0])
        r1.next = None
        r2 = r1
        sum = sum[1::]
        while(sum != []):
            r2 = ListNode(sum[0])
            r2.next = r1
            
            r1 = r2
            sum = sum[1::]
        return r2
        
