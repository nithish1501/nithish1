lst = list(map(int, input().split()))
print("Positive:", sum(1 for x in lst if x > 0))
print("Negative:", sum(1 for x in lst if x < 0))
