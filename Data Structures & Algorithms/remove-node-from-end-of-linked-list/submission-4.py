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

        ele_from_frst = length - n
        count = 0

        temp = head
        prev = head

        while ele_from_frst != count:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = temp.next

        return head
