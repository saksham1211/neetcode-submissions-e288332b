class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.stack2=[]

    def next(self, price: int) -> int:
        span=1
        while self.stack and self.stack[-1]<=price:
            self.stack2.append(self.stack.pop())
            span+=1

        while self.stack2:
            self.stack.append(self.stack2.pop())

        self.stack.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)