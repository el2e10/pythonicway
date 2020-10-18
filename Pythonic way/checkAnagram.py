from collections import Counter

word_one = "python"
word_two = "yhtpon"


def anagram(first, second):
    return Counter(first) == Counter(second)


print("Anagram") if (anagram(word_one, word_two)) else print("Not an anagram")

# Result
# Anagram
