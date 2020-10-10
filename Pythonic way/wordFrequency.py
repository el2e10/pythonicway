from collections import Counter

s = "The quick brown fox jumps over the lazy dog"
freq = dict(Counter(s.lower().split()))

print(f"Sentence:\n{s}")
print(f"\nWord frequencies:\n{freq}")

# Result
# Sentence:
# The quick brown fox jumps over the lazy dog

# Word frequencies:
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
