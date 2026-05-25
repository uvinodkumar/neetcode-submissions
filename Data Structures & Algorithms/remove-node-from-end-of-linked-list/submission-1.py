# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        curr, temp = head, head

        while curr is not None:

            length += 1
            curr = curr.next

        if length == n:
            return head.next

        ele_frm_frst = length - n

        count = 0
        prev = temp
        while ele_frm_frst != count:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = temp.next

        return head
        

        

        