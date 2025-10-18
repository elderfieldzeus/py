def hasdigit(string):
	return any([True if c.isdigit() else False for c in string])

LETTER_LIST = [chr(a) for a in range(ord('A'), ord('Z') + 1)] + [chr(d) for d in range(ord('0'), ord('9') + 1)]
LETTER_MAP = {letter: index for index, letter in enumerate(LETTER_LIST)}

string = input("Enter string: ")

prev = ""

while hasdigit(string) and string != prev:
	new_word = ""

	i = 0
	while i < len(string):
		if i + 1 < len(string) and string[i + 1].isdigit():
			value = LETTER_MAP[string[i]]
			shift = int(string[i + 1])
			new_value = (value - shift + 36) % 36
			new_word += LETTER_LIST[new_value]
			i += 2
		else:
			new_word += string[i]
			i += 1

	prev = string
	string = new_word

print("Result: {}".format(string))