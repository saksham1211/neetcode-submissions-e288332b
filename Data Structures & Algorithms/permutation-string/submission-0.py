class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        countS1 = Counter(s1)
        
        l=0
        r=len(s1)-1

        while r<len(s2):
            count = Counter(s2[l:r+1])
            if count==countS1:
                return True

            l+=1
            r+=1

        return False