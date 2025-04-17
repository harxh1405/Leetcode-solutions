# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = l1, l2
        carry,total,s = 0, 0, 0
        head, tail = None, None
        while carry or i or j:
            total = (i.val if i else 0) + (j.val if j else 0)+ carry
            s, carry = total % 10, total // 10
            node = ListNode(s)
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
            i = i.next if i else None
            j = j.next if j else None
        return head


        