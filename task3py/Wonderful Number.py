
def is_palindrome(s):
    return s == s[::-1]
 
def is_wonderful(n):
    binary = bin(n)[2:] 
    if n % 2 == 0:
        return "NO"
    elif is_palindrome(binary):
        return "YES"
    else:
        return "NO"
 
n = int(input())
print(is_wonderful(n))
