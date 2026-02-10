def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# This won't crash your computer because it doesn't 
# calculate all numbers at once.
gen = infinite_sequence()

print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2