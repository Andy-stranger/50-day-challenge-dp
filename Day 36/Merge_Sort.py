def merge(self,l,m,r,arr):
    temp = []
    ln = l
    rn = m+1
    while ln <= m and rn <= r:
        if arr[ln] < arr[rn]:
            temp.append(arr[ln])
            ln += 1
        else:
            temp.append(arr[rn])
            rn += 1
    while ln <= m:
        temp.append(arr[ln])
        ln += 1
    while rn <= r:
        temp.append(arr[rn])
        rn += 1
    for i in range(len(temp)):
        arr[l+i] = temp[i]
    
def mergeSort(self,arr, l, r):
    if l < r:
        mid = (l+r) >> 1
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(l,mid,r,arr)