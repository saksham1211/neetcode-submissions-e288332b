# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        curr = dummyNode
        carry = 0
        while l1 or l2 or carry:
            res = 0
            res+=l1.val if l1 else 0
            res+=l2.val if l2 else 0
            res+=carry
            if res>=10:
                val = res%10
                remainder = res//10
            else:
                val = res
                remainder = 0

            curr.next = ListNode(val)
            carry=remainder

            curr = curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None


        return dummyNode.next