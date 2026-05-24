class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        if len(self.nums)%2!=0:
            self.median.append(self.nums[len(self.nums)//2])

        else:
            l = self.nums[len(self.nums)//2-1]
            r= self.nums[len(self.nums)//2]
            self.median.append((l+r)/2)

        return

    def findMedian(self) -> float:
        return self.median[-1]
        
        