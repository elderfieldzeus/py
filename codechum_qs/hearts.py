hearts = {1: "H", 2: "E", 3: "A", 4: "R", 5: "T", 6: "S"}

name1 = set("".join(input("Enter first name: ").split()).lower())
name2 = set("".join(input("Enter second name: ").split()).lower())

unique = [i for i in name1 if i not in name2]
unique.extend([i for i in name2 if i not in name1])

ans = len(unique)

print(f"Unique letters is {ans}. Your word is {hearts[ans % 6]}")