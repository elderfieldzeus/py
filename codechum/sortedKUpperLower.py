string = input("Enter string: ")

u = "".join(sorted([c for c in string if c.isupper()]))
l = "".join(sorted([c for c in string if c.islower()]))

k = int(input("Enter k: "))


ans = ""
while k > 0 and u and l:
    ans += u[0] 
    ans += l[0]
    k -= 1
    u = u[1:]
    l = l[1:]
    
ans += u
ans += l 

print("Sorted k word: {}".format(ans))