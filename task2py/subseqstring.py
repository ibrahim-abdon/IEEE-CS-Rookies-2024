def has_hello(s):
    value = "hello"
    index = 0
    for x in s:
        if x == value[index]:
            index += 1
            if index == len(value):
                return "YES"

    return "NO"
s = input().strip()
result = has_hello(s)
print(result)
