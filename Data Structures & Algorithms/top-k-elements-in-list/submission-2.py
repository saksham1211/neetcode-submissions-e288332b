class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[[] for _ in range(len(nums)+1)]
        count = Counter(nums)

        for num, freq in count.items():
            res[freq].append(num)
        
        ans = []

        for i in range(len(res)-1, -1, -1):
            if len(ans)==k:
                return ans

            if res[i]:
                ans.extend(res[i])

        
