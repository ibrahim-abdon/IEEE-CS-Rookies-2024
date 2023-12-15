def print_numbers(n):
    if n > 0:                                
        print_numbers(n - 1)
        print(n)

n = int(input())

print_numbers(n)

# n = int(input())
# if n>=1:
#     for i in range(n):
#         print(i+1)
        


