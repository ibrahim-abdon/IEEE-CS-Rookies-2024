
# Done
from math import factorial
def ncr_npr(a, b):
    ncr = factorial(a) // (factorial(b) * factorial(a - b))
    npr = factorial(a) // factorial(a- b)
    return ncr, npr

a, b = map(int, input().split())

if a >= b:
    result_ncr, result_npr = ncr_npr(a, b)
    
    print(result_ncr, result_npr)
else:
    print("A should be greater than or equal to B")



# n=int(input())
# r=int(input())
# def permutation (n,r):
#     j =2
#     i=n-1
#     result = n*i
#     i = i-1
#     while j < r:
#         result =result *i
#         i = i-1
#         j +=1
#     return result   
# def combination(r):
#     i=1
#     result = r*i
#     while i < r:
#         result = result*i
#         i +=1
#     return permutation(n,r)/result
# if n>=r:
#     print(int(combination(r)) ,  permutation(n,r))
# else:
#     print("Invalid input")
