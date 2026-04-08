class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        dic={}
        res=[]
        for n in nums:
            dic[n]=1+dic.get(n, 0)

        print(dic)
        print(freq)

        for occurance in dic:
            freq[dic[occurance]].append(occurance)

        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                k-=1

            if k==0:
                return res