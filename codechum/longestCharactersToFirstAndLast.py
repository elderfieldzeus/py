string = input("Enter input string: ")

x = input("Enter first character: ")
y = input("Enter second character: ")


mx = (0, 0)

i = 0

while i < len(string):
    if string[i] != x:
        i += 1
        continue
    
    start = i
    while i < len(string) and string[i] == x:
        i += 1
        
    if i - start >= mx[1] - mx[0]:
        mx = (start, i)
        
string = string[mx[0]:mx[1]] + string[:mx[0]] + string[mx[1]:]

i = 0
mx = (0, 0)

while i < len(string):
    if string[i] != y:
        i += 1
        continue
    
    start = i
    while i < len(string) and string[i] == y:
        i += 1
        
    if i - start >= mx[1] - mx[0]:
        mx = (start, i)
        
string =  string[:mx[0]] + string[mx[1]:] + string[mx[0]:mx[1]]

print("First char first, last char last: {}".format(string))