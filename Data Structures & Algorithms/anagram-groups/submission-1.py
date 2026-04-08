class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_list = ["".join(sorted(i)) for i in strs]
        dic = {}

        for i, val in enumerate(sorted_list):
            if val in dic:
                dic[val].append(strs[i])

            else:
                dic[val]=[strs[i]]

        res=[]

        for val in dic.values():
            res.append(val)

        return res