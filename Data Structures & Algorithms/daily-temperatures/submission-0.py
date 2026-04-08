class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0 for i in range(len(temperatures))]
        stack=[[0, temperatures[0]]]

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                previndex=stack.pop()[0]
                res[previndex]=index-previndex

            stack.append([index, temp])

        return res
