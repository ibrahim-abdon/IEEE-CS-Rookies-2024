def get_max(a):
    return max(a)

def get_min(a):
    return min(a)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_prime(a):
    return sum(1 for number in a if is_prime(number))

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def count_palindromes(a):
    return sum(1 for number in a if is_palindrome(number))

def get_max_divisors(a):
    max_divisors = 0
    result = 0
    for number in a:
        divisors_count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                divisors_count += 1
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            result = number
        elif divisors_count == max_divisors and number > result:
            result = number

    return result

number = int(input())
a = list(map(int, input().split()))

print(f"The maximum number : {get_max(a)}")
print(f"The minimum number : {get_min(a)}")
print(f"The number of prime numbers : {get_prime(a)}")
print(f"The number of palindrome numbers : {count_palindromes(a)}")
print(f"The number that has the maximum number of divisors : {get_max_divisors(a)}")


