string = input("Enter string: ")

count = 0

i = 0

while i < len(string):
    count += 1
    prev = string[i]
    while i < len(string) and string[i] == prev:
        i += 1
        
print("Number of segments: {}".format(count))