# Merging Dictionaries (Python 3.9+)
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}

merged = dict_a | dict_b  # The Pipe operator merges them
print(merged)  # {'a': 1, 'b': 3, 'c': 4} (Note: b was updated)

# Extended Iterable Unpacking
first, *middle, last = [1, 2, 3, 4, 5, 6]
print(first)  # 1
print(middle) # [2, 3, 4, 5]
print(last)   # 6