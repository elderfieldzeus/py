string = input("Enter string: ")

words = []

for i in range(len(string)):
    words.append(string)
    string += string[0]
    string = string[1:]

print("Result: {}".format(sorted(words)[0]))