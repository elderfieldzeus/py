string = input("Enter string: ")
k = int(input("Enter k: "))


count = sum([1 for (x, y) in zip(string, string[::-1]) if x != y]) // 2

print("Result: {}".format("Valid" if count <= k else "Invalid"))