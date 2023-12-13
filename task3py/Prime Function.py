def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
t = int(input())
 
if t > 0:
    for _ in range(t):
        n = int(input())
        result = "YES" if is_prime(n) else "NO"
        print(result)
else:
    print("No test cases")
    
