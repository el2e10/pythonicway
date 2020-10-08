
from collections import Counter

s = "The quick brown fox jumps over the lazy dog"
freq = dict(Counter(s.lower().split()))

print(f"Sentence:\n{s}")
print(f"\nWord frequencies:\n{freq}")
