class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity=k
        self.head = ListNode(0)
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            curr = self.head
            while curr.next:
                curr=curr.next
            curr.next = ListNode(value)
            self.size+=1
            return True

        return False

    def deQueue(self) -> bool:
        if not self.head.next:
            return False

        self.head=self.head.next
        self.size-=1
        return True

    def Front(self) -> int:
        if self.head.next:
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if not self.head.next:
            return -1

        curr=self.head.next
        while curr.next:
            curr=curr.next

        return curr.val



    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()