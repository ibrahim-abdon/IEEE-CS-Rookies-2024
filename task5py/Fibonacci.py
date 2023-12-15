def get_sum(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return get_sum(n-1)+get_sum(n-2)
    
n = int(input())

if n>=1:
    result =get_sum(n)
    print(result)