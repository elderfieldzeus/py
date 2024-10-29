size = int(input("Enter size of the first list: "))

l1 = []
l2 = []

for i in range(size):
    temp = input(f"Enter element {i + 1}: ")
    l1.append(int(temp))
    
size = int(input("Enter size of the second list: "))

for i in range(size):
    temp = input(f"Enter element {i + 1}: ")
    l2.append(int(temp))

print(f"Sum of first and last: {l1[0] + l2[-1]}")
print(f"Product of second and second to the last: {l1[1] * l2[-2]}")