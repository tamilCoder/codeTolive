def binary_search(arr, x):

    L = 0
    R = len(arr) - 1
    mid = 0
  
    while L <= R: 
  
        mid = (L + R) // 2          #Finding middle Index
  
        if arr[mid] < x:            #Goes when x is on the RHS
            L = mid + 1
        elif arr[mid] > x:          #Goes when x is on the LHS
            R = mid - 1
        else: 
            return mid              #Goes when we get x
            
    return -1                       #Goes when x is not in the array
  

l = [ 2, 3, 4, 10, 40 ] 
x = 10
ans = binary_search(l, x) 
  
if ans != -1:  
    print("Element is present at index", result) 
else: 
    print("Element is not present in array")
