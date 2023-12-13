def print_numbers(n):
    numbers = ' '.join(str(index) for index in range(1, n+1))
    print(numbers)
 
n = int(input())
print_numbers(n)

