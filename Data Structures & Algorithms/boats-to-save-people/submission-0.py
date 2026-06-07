class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small, large = 0, len(people)-1

        boat=0
        while small<=large:
            total = people[small]+people[large]
            if total<=limit:
                boat+=1
                small+=1
                large-=1

            elif total>limit:
                boat+=1
                large-=1

            
        return boat