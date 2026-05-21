class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {"2":"abc", 
                    "3":"def", 
                    "4":"ghi", 
                    "5":"jkl", 
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        res=[]
        if not digits:
            return []
        def dfs(index, stack):
            print(stack)
            if index==len(digits):
                res.append("".join(stack.copy()))
                return

            ch_list = digit_map[digits[index]]
            for i in range(len(ch_list)):
                stack.append(ch_list[i])
                dfs(index+1, stack)
                stack.pop()

        dfs(0, [])

        return res

            