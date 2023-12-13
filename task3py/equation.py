def get_result(x,n):
    result =0
    i=2
    while i<=n:
        if i %2==0:
            result = int(result + pow(x,i))
        i +=1
    return result

x,n = map(int, input().split())
print (get_result (x,n))
