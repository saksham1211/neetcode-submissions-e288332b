class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while l<r:
            ans=numbers[l]+numbers[r]

            if ans>target:
                r-=1
            if ans<target:
                l+=1

            if ans==target:
                return [l+1, r+1]

        return None
            
