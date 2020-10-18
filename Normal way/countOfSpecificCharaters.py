character_list = ['a', 'e', 'i', 'o', 'u']
word = 'Authorizatioon'
count = 0

for item in word:
    for character in character_list:
        if(item == character):
            count += 1


print(count)

# Result
# 7
