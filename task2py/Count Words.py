s = input()
 
word_count = 0
is_word = False
 
for index in s:
    if index.isalpha():
        is_word = True
    elif is_word:
        word_count += 1
        is_word = False
 
if is_word:
    word_count += 1
 
print(word_count)