def bubbleSort(self,arr):
    n = len(arr)
    for i in reversed(range(n)):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]