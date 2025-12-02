int_name_='_main_'
arr=[5,4,4,6,2,6]
lst=sorted(arr)
idx=1
for i in range(1,len(lst)):
  if lst[i]!=lst[i-1]:
        lst[idx]=lst[i]
        idx+=1
for i in range(idx):
    print(lst[i], end=" ")

'''def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return n

    idx = 1  # Start from the second element
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx

# Driver code
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newSize = removeDuplicates(arr)
print(arr)
for i in range(newSize):
    print(arr[i], end=" ")'''
