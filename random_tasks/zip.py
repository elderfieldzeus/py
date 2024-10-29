size = int(input("Enter size: "))

list1 = []
list2 = []

for i in range(size):
    list1.append(int(input()))

for i in range(size):
    list2.append(int(input()))

product_list = [a * b for a,b in zip(list1, list2)]
print(product_list)