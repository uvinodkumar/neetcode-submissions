# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next

        if length == n:
            return head.next

        ele_frm_frst = length - n

        prev = head 
        temp = head
        i = 0

        while i != ele_frm_frst:
            prev = temp
            temp = temp.next
            i += 1
        
        prev.next = temp.next

        return head
        

