
# def array_average(n,list_n):
#     sum =0
#     for index in list_n:
#         sum =sum+index
#     print(f"{sum/n:.6f}")
# n = int(input())
# list_n=  list(map(int,input().split()))
# array_average(n,list_n)


# so to do recursion sum must be sent with the function to renew its value

def array_average(arr, n, sum=0, index=0):
    sum=sum
    if index == n:
        return sum / n
    return array_average(arr, n, sum + arr[index], index + 1 )

n = int(input())
list_n = list(map(int, input().split()))

result = array_average(list_n, n)
print(f'{result:.6f}')



