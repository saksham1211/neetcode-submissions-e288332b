class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)

            else:
                if stack:
                    current_char=stack.pop()

                    if char==")" and current_char!="(":
                        return False

                    if char=="}" and current_char!="{":
                        return False

                    if char=="]" and current_char!="[":
                        return False

                else:
                    stack.append(char)


        if not stack:
            return True

        else:
            return False
