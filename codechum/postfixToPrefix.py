exp = []

ans = ""

while True:
    ans = input("Enter: ")

    if ans == "x":
        break

    if ans.isdigit():
        exp.append(ans)
    else:
        y = exp.pop()
        x = exp.pop()

        exp.append("{} {} {}".format(ans, x, y))

print("Prefix: {}".format("".join(exp)))