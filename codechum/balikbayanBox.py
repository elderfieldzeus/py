name = input("Enter name: ")

size = 0

while size < len(name) + 2:
    size = int(input("Enter box size: "))


print("*" * size)

for i in range(size // 2 - 2):
    if i == ((size // 4) - 1):
        print("*" + name.center(size - 2) + "*")
    else:
        print("*" + " " * (size - 2) + "*")


print("*" * size)