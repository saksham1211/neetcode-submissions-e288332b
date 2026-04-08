class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        sorted_strs=[''.join(sorted(s)) for s in strs]
        dic={} # sorted key: [original value]

        for i in range(len(sorted_strs)):
            if sorted_strs[i] in dic:
                dic[sorted_strs[i]].append(strs[i])

            else:
                dic[sorted_strs[i]]=[strs[i]]


        for val in dic.values():
            res.append(val)

        return res