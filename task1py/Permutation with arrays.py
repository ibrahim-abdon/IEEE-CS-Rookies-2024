n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#  order from small to big
a.sort()
b.sort()
# احنا لما نرتبهم فالمفروض كل عنصر هيساوي المقابل ليه

for i in range(n):
    if a[i] != b[i]:
        print("no")
        exit()
 
print("yes")



# does not work ---->
# def is_b_permutation_a(a,b,n):
#     j=0
#     i=0
#     while i<len(a) and j <len(b):
#         if a[i]==b[j]:
#             j += 1
#             i =0
#         else:
#             i +=1
#     if(j==len(b)):
#         return "yes"
#     else:
#         return "no"
     
# n =int(input())
# a=list(map(int, input().split()))
# b=list(map(int, input().split()))
# print(is_b_permutation_a(a,b,n))