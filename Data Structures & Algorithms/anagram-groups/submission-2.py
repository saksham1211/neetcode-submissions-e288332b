class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = ["".join(sorted(list(word))) for word in strs]
        dic=defaultdict(list)

        for i, word in enumerate(strs):
            dic[sorted_list[i]].append(strs[i])

        res=[]

        for i in dic:
            res.append(dic[i])

        return res

            