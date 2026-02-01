nums = [1, 2, 3, 4, 5]

squares = [n*n for n in nums]
even_map = {n: n*n for n in nums if n % 2 == 0}
unique_lengths = {len(word) for word in ["hi", "hello", "hi"]}

print(squares, even_map, unique_lengths)