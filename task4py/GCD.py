# Done

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a
 
def lcm(a, b):
    return (a // gcd(a, b)) * b
 
a, b = map(int, input().split())
 
print(str(gcd(a, b)) + " " + str(lcm(a, b)))



# def gcd(a, b):
#     while b != 0:
#         temp =a
#         a = b
#         b = temp % a
#     return a

# def lcm (a,b):
#     return (a/gcd(a,b)) * b

# a = int(input())
# b = int(input())

# print(str(int(gcd(a, b))) + " " + str(int(lcm(a, b))))