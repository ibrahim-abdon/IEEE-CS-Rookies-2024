q = int(input())
s = input()

key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

result = ""

if q == 1:  
    for index in s:
        if index in original:
            index = original.index(index)
            result += key[index]
elif q == 2:  
    for index in s:
        if index in key:
            index = key.index(index)
            result += original[index]

print(result)
