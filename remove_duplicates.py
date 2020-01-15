                                                 '''REMOVE DUPLICATES IN ARRAY'''

#BruteForceApproach......Aproach 1

def RemoveDuplicates( arr, size):
    k = 0
    arr[k] = arr[0];

    for i in range(1,size):
        for j in range(i+1,size):
            if(arr[j]==arr[i]):
                arr[j] = arr[0]

        if(arr[i]!=arr[0]):
            k += 1
            arr[k] = arr[i]
    #size = k+1;
    return k+1

arr=[12,65,12,65,20,12,20,17,17,28,85]

size = len(arr)

size = RemoveDuplicates(arr,size)

print(arr[:size])

#Aproach 2

arr=[12,65,12,65,20,12,20,17,17,28,85]

original=[]

for element in arr:
    if element not in original:
        original.append(element)
print(original)

#Aproach 3 (Only for sorted array)

arr=[0,0,1,2,2,3,4,5,5,5,5,6,9]

king=0

for i in range(1, len(arr)):
    if arr[i] != arr[king]:
        king += 1
        arr[king] = arr[i]

print(arr[:king+1])
