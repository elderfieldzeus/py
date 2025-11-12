n = int(input("Enter n: "))
m = int(input("Enter m: "))

grid = []

print("Input grid: ")
for i in range(n):
    grid.append(list(map(int, input().split())))
    
h = (0, n - 1)
v = (0, m - 1)

while h[0] < h[1] or v[0] < v[1]:
    xor = 0
    for i in range(h[0], h[1] + 1):
        for j in range(v[0], v[1] + 1):
            if i == h[0] or i == h[1] or j == v[0] or j == v[1]:
                xor ^= grid[i][j]
                
    for i in range(h[0], h[1] + 1):
        for j in range(v[0], v[1] + 1):
            if i == h[0] or i == h[1] or j == v[0] or j == v[1]:
                grid[i][j] += xor
                
    h = (h[0] + 1, h[1] - 1)
    v = (v[0] + 1, v[1] - 1)
    
print("\nNew grid: ")

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
        
    print("")