# Sample output: 
# Enter encoded string: 5[ab2[c]3[d]]
# Result: abccdddabccdddabccdddabccdddabccddd

def create_string(string, index):
    times = 0

    while index[0] < len(string) and string[index[0]].isdigit():
        times = times * 10 + int(string[index[0]])
        index[0] += 1

    index[0] += 1

    word = ""
    while index[0] < len(string) and string[index[0]] != "]":
        if string[index[0]].isdigit():
            word += create_string(string, index)
        else:
            word += string[index[0]]
            index[0] += 1

    index[0] += 1

    return times * word


string = input("Enter encoded string: ")

index = [0]
ans = ""

while index[0] < len(string):
    ans += create_string(string, index)

print("Result: ", ans)