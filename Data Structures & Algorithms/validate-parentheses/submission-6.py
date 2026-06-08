class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char not in ["{", "[", "("]:
                if char == "}":
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        stack.append(char)
                    
                if char =="]":
                    if stack and stack[-1]=="[":
                        stack.pop()
                    else:
                        stack.append(char)
                        
                if char==")":
                    if stack and stack[-1]=="(":
                        stack.pop()

                    else:
                        stack.append(char)
                        
            else:
                stack.append(char)


        return True if not stack else False