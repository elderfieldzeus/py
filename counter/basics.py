from collections import Counter

s = input("Input a string to be counted: ")

counter = Counter(s.lower())

print(counter)

print("Accessing elements: ", )

for i in counter:
    print("{}: {}", i, counter[i])

print(counter.most_common()) # returns list of elements sorted in descending order by its count