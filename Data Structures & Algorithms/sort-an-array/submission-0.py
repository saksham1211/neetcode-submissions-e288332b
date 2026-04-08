class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## merge sort

        def merge(left, right):
            l, r =0, 0
            res=[]
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r+=1

            res.extend(left[l:])
            res.extend(right[r:])

            return res



        def mergeSort(arr):
            if len(arr)<=1:
                return arr
            l=0
            r=len(arr)
            mid = (l+r)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        
        return mergeSort(nums)