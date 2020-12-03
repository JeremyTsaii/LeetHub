# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        arr = []
        
        for link in lists:
            while(link):
                arr.append(link.val)
                link = link.next
        
        arr.sort()
        head = ListNode(0)
        cur = head
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        
        return head.next
