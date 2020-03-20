n = int(input('Please enter number of n:\n'))
arr = []
print('Now, please enter n * n items of array:\n')
for i in range(n):
    items = input().split(' ')
    for j in range(0, len(items)): 
        items[j] = int(items[j]) 
    arr.append(items)
    
print('\nMatrix is: \n', arr)
    
from math import ceil 

MAX = 99999999
positions = []
  
def findMax(arr, n, mid,max): 
    max_index = 0
    for i in range(n): 
        if (max < arr[i][mid]): 
            max = arr[i][mid] 
            max_index = i 
    return max,max_index 
  
def findPeakRec(arr, n, mid): 
    max = 0
    max, max_index = findMax(arr, n, mid, max) 
    positions.append((max_index, mid))
    if (mid == 0 or mid == n - 1): 
        return max  
    if (max >= arr[max_index][mid - 1] and max >= arr[max_index][mid + 1]): 
        return max  
    if (max < arr[max_index][mid - 1]): 
        return findPeakRec(arr, n, mid - ceil(mid / 2.0))   
    return findPeakRec(arr, n, mid + ceil(mid / 2.0)) 
  
def findPeak(arr, n): 
    return findPeakRec(arr, n, n // 2) 

print('\n----Answer-----') 
print('Peak Element is:', findPeak(arr, n)) 
print('Peak Element position is:',positions[-1])