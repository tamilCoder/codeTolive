def linear_search(arr, x): 

	for i in range(len(arr)): 

		if arr[i] == x: 
			return i 

	return -1

l = [5, 0, 12, 7, 1, 10] 
x = 1
ans = linear_search(l, x) 
  
if ans != -1:  
    print("Element is present at index", ans) 
else: 
    print("Element is not present in array")
