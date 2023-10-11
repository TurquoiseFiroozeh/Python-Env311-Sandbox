"This code is all about loop and iteration"

NUMS = [1, 2, 3, 4, 5]

for num in NUMS:
    print(num)

print("\nbreak in a loop")

for num in NUMS:
    if num == 3:
        print(f"{num} Found!")
        break
    print(num)

print("\nContinue in a loop")

for num in NUMS:
    if num == 3:
        print("Found!")
        continue
    print(num)

print("\n Inner/Nested Loop in a loop")

for num in NUMS:
    for letter in 'abc':
        print(num, letter)

print("\n enumrate in a loop start at 0")
for i in range(10):
    print(i)


print("\n enumrate in a loop start at 1")
for i in range(1, 11):
    print(i)

print("\n while loop")
X = 0
while X < 10:
    print(X)
    X += 1

print("\n while loop with break")
X = 0
while X < 10:
    if X == 5:
        break
    print(X)
    X += 1


print("\n infinit loop")
X = 0
while True:
    if X == 5:
        break
    print(X)
    X += 1


print("\n stop infinit loop with ctr+c")
X = 0
while True:
    # if X == 5:
    #     break
    print(X)
    X += 1
