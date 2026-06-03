class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPali(s[i:j]):
                    res+=1

        return res
    
    def isPali(self, s):
        l=0
        r=len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1

        return True

        


