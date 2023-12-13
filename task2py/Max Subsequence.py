n = int(input())
s = input()
 
max_size = 0
prev_char = ''
 
for index in s:
    if index != prev_char:
        prev_char = index
        max_size += 1
 
print(max_size)