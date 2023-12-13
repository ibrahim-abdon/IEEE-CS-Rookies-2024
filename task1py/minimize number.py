def maximize_number(n, arr):
    max_operations = 0

    # Check if all numbers are divisionable 2
    while all(number % 2 == 0 for number in arr):    
        # so this is the new list 
        arr = [number // 2 for number in arr]
        max_operations += 1

    return max_operations

n = int(input())
list_numbers = list(map(int, input().split()))
result = maximize_number(n,list_numbers)
print(result)

