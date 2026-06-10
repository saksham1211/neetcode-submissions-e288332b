# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        secondList = slow.next
        slow.next = None

        prev=None
        curr=secondList
        while curr:
            temp=curr.next
            curr.next = prev
            prev = curr
            curr=temp

        head2 = prev

        dummyNode = ListNode(0)
        dummyNode.next = head

        while head and head2:
            temp = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp
            head=temp
            head2=temp2

        
