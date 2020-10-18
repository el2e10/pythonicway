import re

character_list = 'aeiou'
word = 'Authorizatioon'

count = len(re.findall(r'[aeiou]', word))

print(count)

# Result
# 7
