class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for char in tokens:
         
            if char == "+":
                if len(stack)>=2:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a+b)

            elif char == "*":
                if len(stack)>=2:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)

            elif char == "/":
                if len(stack)>=2:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b/a))

            elif char =="-":
                if len(stack)>=2:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)

            else:
                stack.append(int(char))
            
        return stack[0]