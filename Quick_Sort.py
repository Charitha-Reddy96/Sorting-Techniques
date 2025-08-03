
def Partion(arr,low,high):
    i ,j = low, high
    pivot = arr[low]
    while i <= j:    
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    arr[j] , arr[low] = arr[low] , arr[j]
    return j 

def Quick_Sort(arr,low,high):
    if low < high:    
        partition = Partion(arr,low,high)
        Quick_Sort(arr,low,partition)
        Quick_Sort(arr,partition+1,high)

arr = [4,6,2,5,7,9,1,3]
Quick_Sort(arr,0,len(arr)-1)
print(arr)