n = int(input("Input number: "))

matrix = [[0] * n for _ in range(n)] 

left = 0
right = n - 1
top = 0
bottom = n - 1

i = 0
j = 0
num = 1
while num <= n ** 2:
    while num <= n ** 2 and j <= right:
        matrix[i][j] = num
        num += 1
        j += 1

    i += 1
    j -= 1
    top += 1

    while num <= n ** 2 and i <= bottom:
        matrix[i][j] = num
        num += 1
        i += 1

    j -= 1
    i -= 1
    right += 1

    while num <= n ** 2 and j >= left:
        matrix[i][j] = num
        num += 1
        j -= 1

    i -= 1
    j += 1
    bottom -= 1

    while num <= n ** 2 and i >= top:
        matrix[i][j] = num
        num += 1
        i -= 1

    j += 1
    i += 1
    top += 1

for m in matrix:
    for i in m:
        print(i, end=" ")
    print()