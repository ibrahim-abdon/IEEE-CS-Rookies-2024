def shift_item(a, x):
    if len(a) > 0:
        x %= len(a)  
        for i in range(x):
            last_item = a.pop()
            a.insert(0, last_item)
        return a
    else:
        return 'List must not be empty'

n, x = map(int, input().split())
a = list(map(int, input().split()))

result = shift_item(a, x)
print(*result)


