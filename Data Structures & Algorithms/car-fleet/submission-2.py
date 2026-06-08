class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]

        cars.sort(key=lambda x:x[0])

        stack = []

        for i in range(len(cars)-1, -1, -1):
            t = (target-cars[i][0])/cars[i][1]

            if not stack:
                stack.append(t)

            else:
                if stack[-1]<t:
                    stack.append(t)

        
        return len(stack)