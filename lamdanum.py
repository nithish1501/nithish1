nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x*x, nums))

print(evens, squares)