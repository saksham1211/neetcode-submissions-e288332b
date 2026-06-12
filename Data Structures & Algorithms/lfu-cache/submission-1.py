class ListNode:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.freq=1
        self.prev=None
        self.next=None

    
class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        self.size=0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev=prev
        node.next=self.right
        self.right.prev = node
        self.size+=1

    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev=None
        node.next=None
        self.size-=1
        return node

    def popLeft(self):
        if self.length()==0:
            return None

        node = self.left.next
        self.left.next = node.next
        node.next.prev = self.left
        node.prev=None
        node.next=None
        self.size-=1
        return node

## ll to keep track of ordering like LRU
## key to node mapping 
## lfu counter to keep track of least frquent bucket in cache

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeMap = {} 
        self.listMap = defaultdict(LinkedList)
        self.lfuCnt = 0
        
    def counter(self, node):
        cnt = node.freq
        self.listMap[node.freq].pop(node)

        if cnt==self.lfuCnt and self.listMap[cnt].length()==0:
            self.lfuCnt+=1

        node.freq+=1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self.counter(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return

        if len(self.nodeMap)==self.cap:
            lfu = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(lfu.key)
           

        node = ListNode(key, value)
        self.nodeMap[key]=node
        self.listMap[1].pushRight(node)
        self.lfuCnt=1




            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)