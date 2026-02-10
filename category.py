from collections import Counter, default
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts["apple"])  
groups = defaultdict(list)
data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "pear")]
for category, item in data:
    groups[category].append(item)

print(dict(groups)) 