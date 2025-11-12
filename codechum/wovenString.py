s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

s = ""

while s1 and s2:
    if len(s1) < len(s2):
        if s1 == s2[:len(s1)]:
            s += s2[0]
            s2 = s2[1:]
            continue
    if len(s2) < len(s1):
        if s2 == s1[:len(s2)]:
            s += s1[0]
            s1 = s1[1:]
            continue
        
    if s1 < s2:
        s += s1[0]
        s1 = s1[1:]
    else:
        s += s2[0]
        s2 = s2[1:]
        
s += s1
s += s2

print("Woven string: {}".format(s))