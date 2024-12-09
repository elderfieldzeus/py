size = int(input("Enter size of matrix: "))

matrix = []

for i in range(size):
    matrix.append(input())

fav = input("Enter favorite number: ")

matrix = sorted(matrix, key = lambda m : m.count(fav), reverse=True)

for i in matrix:
    print(i)