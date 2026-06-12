class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev =self.left
        

    def add(self, node):
        prev, nxt = self.left, self.left.next
        self.left.next = node
        node.prev=self.left
        nxt.prev=node
        node.next=nxt

    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.add(node)
            return node.val

        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            node = ListNode(key, value)
            self.hashMap[key]=node
            self.add(node)

        else:
            node = ListNode(key, value)
            self.hashMap[key]=node
            self.add(node)

        if len(self.hashMap)>self.cap:
            lru=self.right.prev
            self.remove(lru)
            print(lru.key)
            del self.hashMap[lru.key]

        
        
