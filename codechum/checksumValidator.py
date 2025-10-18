string = input("Enter string: ")
key = int(input("Enter key: "))

index = 0

s = 0
while index < len(string):
    letter = string[index]
    index += 1

    digit = 0

    while index < len(string) and string[index].isdigit():
        digit *= 10
        digit += int(string[index])
        index += 1

    s += ord(letter) * digit

print("Result: {}".format("Valid" if s % key == 0 else "Corrupt"))