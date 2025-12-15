"""def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
n=5
res=fact(n)
print(res)"""
def fact(n):
    if n ==0 or n == 1:
        return 1
    result = n * fact(n-1)
    return result
res= fact(5)
print(res)