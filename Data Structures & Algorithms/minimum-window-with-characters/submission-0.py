class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window={}
        have = 0
        need = len(countT)
        l=0
        resLen = float("inf")
        res=[-1, -1]
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1

            while have==need:
                if (r-l+1)<resLen:
                    res = [l, r]
                    resLen = r-l+1
            
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1

                l+=1

        l, r = res
        return s[l:r+1] if resLen!=float("inf") else ""
        