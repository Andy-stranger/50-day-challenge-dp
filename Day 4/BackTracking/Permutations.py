from typing import List

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def getPermutations(ind,arr):
            if ind == len(arr):
                ans.append(arr[:])
                return
            for i in range(ind,len(arr)):
                arr[i],arr[ind] = arr[ind],arr[i]
                getPermutations(ind+1,arr)
                arr[i],arr[ind] = arr[ind],arr[i]
            return
        getPermutations(0,nums)
        return ans
