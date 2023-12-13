def max_subarray(n, list_numbers):
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray = list_numbers[i:j]
            max_number = max(subarray)
            result.append(max_number)
    return result

input_value = int(input())

for i in range(input_value):
    n = int(input())
    list_numbers = list(map(int, input().split()))

    result = max_subarray(n, list_numbers)
    print(*result)








# usage
# arr = [1, 2, 3, 4, 5]
# subarray = arr[1:4]
# print(subarray)