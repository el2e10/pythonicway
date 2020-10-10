sample_dict = {'Turtles':5, 'Dogs':3, 'Cats':3, 'Snakes':2}
max_key = max(sample_dict, key=sample_dict.get)

print(f"In the dictionary, there are the most {max_key} ({sample_dict[max_key]}).")

# Result
# In the dictionary, there are the most Turtles (5).
