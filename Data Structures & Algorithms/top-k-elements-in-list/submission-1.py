class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]

        count = Counter(nums)

        for num, c in count.items():
            freq[c].append(num)

        res = []

        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                res.extend(freq[i])

            if len(res)==k:
                return res