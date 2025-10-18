string = input("Enter a string: ")

u, l, d, s = 0, 0, 0, 0

for c in string:
	if c.isupper():
		u += 1
	elif c.islower():
		l += 1
	elif c.isdigit():
		d += 1
	else:
		s += 1

print("Uppercase letters: {}".format(u))
print("Lowercase letters: {}".format(l))
print("Digits: {}".format(d))
print("Symbols: {}".format(s))