def isASubOfB (n,m,list_n,list_m):
    i =0
    j =0
    while i <len(list_n) and j<len(list_m):
        if list_n[i] == list_m[j]:
            j +=1
        i +=1
    if j == len(list_m):
        return "YES"
    else:
        return "NO"
    
n,m= map( int , input().split())
list_n = list(map(int, input().split()))
list_m = list(map(int, input().split()))
result=isASubOfB(n,m,list_n,list_m)
print(result)