# n = 3
#  ^
# / \
#<   >
# \ /
#  v

n = int(input("Enter n: "))

size = n * 2 - 1
left = n
right = n

for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == n and i == 1:
            print("^", end="")
        elif j == n and i == size:
            print("v", end="")
        elif i == n and j == 1:
            print("<", end="")
        elif i == n and j == size:
            print(">", end="")
        elif j == left:
            print("/", end="")
        elif j == right:
            print("\\", end="")
        else:
            print(" ", end="")

    print()
    left = left - 1
    right = right + 1

    if left < 1:
        left = n * 2 - 2
    if right > n * 2 - 1:
        right = 2
