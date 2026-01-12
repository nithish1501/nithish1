n = input("Enter number: ")
total = 0
for digit in n:
    total += int(digit) ** len(n)

if total == int(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
