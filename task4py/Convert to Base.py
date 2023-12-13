# Done
t = int(input())
n, x = input().split()

if t == 1:
    decimal_value = int(n, int(x))
    print(decimal_value)
elif t == 2:
    decimal_value = int(n)
    base_X_value = ''
    while decimal_value > 0:
        remainder = decimal_value % int(x)
        if remainder < 10:
            base_X_value = str(remainder) + base_X_value
        else:
            base_X_value = chr(ord('A') + remainder - 10) + base_X_value
        decimal_value //= int(x)
    print(base_X_value)