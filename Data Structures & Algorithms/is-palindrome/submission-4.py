class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<j:
            while i<j and not s[i].isalpha() and not s[i].isdigit():
                i+=1

            while i<j and not s[j].isalpha() and not s[j].isdigit():
                j-=1

            if s[i].lower()!=s[j].lower():
                return False

            i+=1
            j-=1
        
        return True