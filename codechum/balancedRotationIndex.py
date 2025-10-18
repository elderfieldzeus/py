import math

size = int(input("Enter array size: "))

print("Enter the elements: ")
elems = list(map(int, input().split()))

minValue = math.inf
minIndex = 0

for i in range(size):
    currentSum = 0
    for j in range(size):
        currentSum += j * elems[j]

    if currentSum < minValue:
        minIndex = i
        minValue = currentSum

    elems.append(elems[0])
    elems.pop(0)

print("Balanced Rotation Index: {}".format(minIndex))
