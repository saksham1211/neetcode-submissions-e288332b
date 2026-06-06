class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            j=0
            while j<len(res) and j<len(word) and res[j]==word[j]:
                j+=1

            res=word[:j]

        return res