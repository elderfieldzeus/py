def bfs(grid, size, x, y, prev, thresh, stable_zone):
    if x >= size or y >= size:
        return

    if abs(grid[x][y] - prev) <= thresh:
        stable_zone.add((x,y))
        bfs(grid, size, x + 1, y, grid[x][y], thresh, stable_zone)
        bfs(grid, size, x, y + 1, grid[x][y], thresh, stable_zone)

n, t = list(map(int, input("Enter n and t: ").split()))

grid = []
print("Enter the grid:")
for i in range(n):
	row = list(map(int, input().split()))
	grid.append(row)

max_zone = 0
max_pair = (0, 0)
for i in range(n):
    for j in range(n):
        value = grid[i][j]
        stable_zone = set()
        stable_zone.add(value)

        bfs(grid, n, i + 1, j, value, t, stable_zone)
        bfs(grid, n, i, j + 1, value, t, stable_zone)

        if len(stable_zone) > max_zone:
            max_zone = len(stable_zone)
            max_pair = (i, j)

print("Largest stable zone found at {} with size: {}".format(max_pair, max_zone))