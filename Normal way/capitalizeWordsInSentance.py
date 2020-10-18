sentance = "this is a test sentance"

sentance_split = sentance.split(' ')

for key, word in enumerate(sentance_split):
    sentance_split[key] = word.capitalize()

sentance = " ".join(sentance_split)

print(sentance)

# Result
# This Is A Test Sentance
