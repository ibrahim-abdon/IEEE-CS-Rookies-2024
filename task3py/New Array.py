
def sum_list(a, b):
    sum = b + a
    return sum

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = sum_list(a, b)
print(*result)
