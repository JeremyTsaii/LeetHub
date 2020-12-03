# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry = 0
        head = ListNode(0)
        cur = head
        while(p1 or p2):
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2: 
                val += p2.val
                p2 = p2.next
            carry = val//10
            val = val%10
            cur.next = ListNode(val)
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return head.next
