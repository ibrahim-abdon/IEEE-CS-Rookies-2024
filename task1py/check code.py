def check_code(a, b, code):
    if len(code) != a + b + 1:
        return "No"

    if code[a] != '-':
        return "No"

    for i in range(a):
        if not code[i].isdigit():
            return "No"
    
    for i in range(a + 1, a + b + 1):
        if not code[i].isdigit():
            return "No"

    return "Yes"

a, b = map(int, input().split())
code = input()

result = check_code(a, b, code)
print(result)
