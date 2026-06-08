class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op=="+":
                if len(stack)>=2:
                    a=stack[-1]
                    b=stack[-2]
                    stack.append(a+b)

            elif op=="D":
                if stack:
                    a = stack[-1]
                    stack.append(a*2)

            elif op=="C":
                if stack:
                    stack.pop()

            
            else:
                stack.append(int(op))


        return sum(stack)
