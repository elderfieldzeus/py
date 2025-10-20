s1 = input('Enter the first string: ')
s2 = input('Enter second string: ')

ans = ""
secondStart = 0

for i in range(len(s1)):
    for j in range(secondStart, len(s2)):
        if s1[i] == s2[j]:
            ans += s1[i]
            secondStart = j
            break

if ans != "":
    print("The longest common subsequence is {}.".format(ans))

else:
    print("There is no common subsequence between the two strings.")