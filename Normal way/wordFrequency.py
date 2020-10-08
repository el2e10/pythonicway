
s = "The quick brown fox jumps over the lazy dog"

word = ""
s += " "
freq = {}

for i in range(len(s)):
    ch = s[i].lower()
    if ch != ' ':
        word += ch
    else:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
        word = ""

print("Sentence:\n" + s)
print("\nWord frequencies:\n" + str(freq))
