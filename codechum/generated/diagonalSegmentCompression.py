"""
🔷 Programming Problem: Diagonal Segment Compression

You are given an 
𝑛
×
𝑚
n×m matrix of integers.
We define a diagonal segment as a maximal sequence of elements that lie on the same top-left → bottom-right diagonal and that also have the same value.

For example, in this matrix:

3 3 2
3 1 1
4 1 1


The diagonal starting at (0,0) contains values:
3, 1, 1 → but has two segments:

[3]

[1, 1]

Task

For each diagonal (starting either in the first row or in the first column), compute:

The number of diagonal segments.

The length of the longest diagonal segment.

Then output:

The total number of diagonal segments across the whole matrix.

The maximum segment length among all diagonals.

Input Format
n m
a11 a12 ... a1m
...
an1 an2 ... anm

Output Format
total_segments max_segment_length

Example
Input
3 3
3 3 2
3 1 1
4 1 1

Explanation of diagonals

Start (0,0): 3 → 1 → 1
segments = 2, longest = 2

Start (0,1): 3 → 1
segments = 2, longest = 1

Start (0,2): 2
segments = 1, longest = 1

Start (1,0): 3 → 1
segments = 2, longest = 1

Start (2,0): 4
segments = 1, longest = 1

Total segments = 2+2+1+2+1 = 8
Max segment length = 2

Output
8 2
"""

n, m = list(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(n)]

def getDiagonalSegments(x, y):
    a = []
    while x < n and y < m:
        a.append(grid[x][y])
        x += 1
        y += 1
        
    num_segments, max_segment = 0, 0
    
    i = 0
    
    
    while i < len(a):
        prev = a[i]
        cnt = 0
        
        while i < len(a) and a[i] == prev:
            i += 1
            cnt += 1
            
        num_segments += 1
        max_segment = max(cnt, max_segment)
        
    return num_segments, max_segment
    
n_seg, m_seg = 0, 0

for i in range(m):
    nn, mm = getDiagonalSegments(0, i)
    n_seg += nn
    m_seg = max(mm, m_seg)
    
for i in range(1, n):
    nn, mm = getDiagonalSegments(i, 0)
    n_seg += nn
    m_seg = max(mm, m_seg)
    
print(n_seg, m_seg)