def is_good_or_bad(s):
    if "010" in s or "101" in s:
        return "Good"
    else:
        return "Bad"
 
t = int(input())
 
for x in range(t):
    S = input().strip()
    
    result = is_good_or_bad(S)
    print(result)