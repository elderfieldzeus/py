string = input("Enter name: ")

mx = 0

i = 0

while i < len(string):
    val = string[i]
    count = 0
    
    while i < len(string) and string[i] == val:
        count += 1
        i += 1
        
    mx = max(count, mx)
    
print("The max subsequence is: {}".format(mx))