'''if __name__ == '__main__':
    a=input("enter the elements: ")
    n=a.split()
    key=5
    lst=[int(i) for i in n]
    if key in lst:
        lst.remove(key)
    else:
        print("no key")
    #n=lst.append(int(input()))
    # for i in range(0,con):
        #n=int(input().split())
        lst.append(i)
    #print (sorted(lst))
    print(lst)'''
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5, 6]
    n = len(arr)
    #for i in range(n - 1, 0, -1):
   #     arr[i] = arr[i - 1]
  #  arr[0] = arr[n-1]
#arr.sort()
#result=list(reversed(arr))
result= sorted(arr)
arr2=list(reversed(result))
print(result)
print(arr2)


#print(sorted(arr))
#print(arr[i],end=" ")