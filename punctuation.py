import string
s = input()
print("".join(ch for ch in s if ch not in string.punctuation))
