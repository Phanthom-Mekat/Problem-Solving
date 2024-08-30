# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            arr[-1]=-1
            return arr
        top= -1
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = top
            # print(top,temp)
            # print(max(top,temp))
            top = max(top, temp)
        return arr





