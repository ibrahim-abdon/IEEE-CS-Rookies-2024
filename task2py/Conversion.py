def convert_string(s):
    s = s.replace(',', ' ')
    s = s.swapcase()
    return s
s = input().strip()
result = convert_string(s)
print(result)
