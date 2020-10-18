word_one = "python"
word_two = "yhtppon"


def checkAnagram(word_one, word_two):
    for i in word_one:
        if(i in word_two):
            word_two = word_two.replace(i, '', 1)
        else:
            print("Not an anagaram")
            return
    print("Anagram") if(len(word_two) == 0) else print("Not an anagram")


checkAnagram(word_one, word_two)

# Result
# Not an anagram
