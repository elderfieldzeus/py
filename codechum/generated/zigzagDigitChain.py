"""
# Zigzag Digit Chain

## Problem Description

Given an array of positive integers, find the length of the longest **zigzag digit chain**. A zigzag digit chain is a subsequence of consecutive elements from the array that satisfies these conditions:

1. The number of digits must alternate between "more" and "fewer" for each consecutive pair
   - If element[i] has more digits than element[i-1], then element[i+1] must have fewer digits than element[i]
   - If element[i] has fewer digits than element[i-1], then element[i+1] must have more digits than element[i]

2. For each consecutive pair in the chain, the last digit of the first number must be strictly less than the first digit of the second number

3. A valid chain must contain at least 2 elements

The chain must consist of consecutive elements from the original array (no skipping allowed).

## Input

**Line 1:** An integer n representing the size of the array (2 ≤ n ≤ 100000)

**Line 2:** n space-separated positive integers (1 ≤ each integer ≤ 10^9)

## Output

A single integer representing the length of the longest zigzag digit chain. If no valid chain exists, output 1.

## Constraints

- 2 ≤ n ≤ 100000
- 1 ≤ array elements ≤ 10^9
- All inputs are positive integers

## Sample Test Cases

### Sample Input #1
```
Enter size: 6
Enter elements:
11 567 83 945 21 6
```

### Sample Output #1
```
Longest zigzag digit chain: 4
```

**Explanation:** The chain is [11, 567, 83, 945]
- 11 (2 digits, last=1) → 567 (3 digits, first=5): More digits ✓, 1 < 5 ✓
- 567 (3 digits, last=7) → 83 (2 digits, first=8): Fewer digits ✓, 7 < 8 ✓  
- 83 (2 digits, last=3) → 945 (3 digits, first=9): More digits ✓, 3 < 9 ✓

### Sample Input #2
```
Enter size: 5
Enter elements:
7 88 2 345 91
```

### Sample Output #2
```
Longest zigzag digit chain: 3
```

**Explanation:** Chain is [2, 345, 91]:
- 2 → 345: 2 < 3 ✓, more digits ✓
- 345 → 91: 5 < 9 ✓, fewer digits ✓
Length = 3 ✓

### Sample Input #3
```
Enter size: 4
Enter elements:
100 25 678 12
```

### Sample Output #3
```
Longest zigzag digit chain: 3
```
"""


size = int(input("Enter size: "))
arr = list(map(int, input("Enter elements:\n").split()))

mx_digits = 1
should_be_greater = False

for i in range(size - 1):
    should_be_greater = len(str(arr[i])) < len(str(arr[i + 1]))

    if int(str(arr[i])[-1]) >= int(str(arr[i + 1])[0]):
        continue

    cnt = 2
    for j in range(i + 1, size - 1):
        x, y = len(str(arr[j])), len(str(arr[j + 1]))
        
        
        if (should_be_greater and x > y) or (not should_be_greater and x < y):
            if int(str(arr[j])[-1]) < int(str(arr[j + 1])[0]):
                cnt += 1
                should_be_greater = not should_be_greater
                continue

        break
    
    mx_digits = max(mx_digits, cnt)

print("Longest zigzag digit chain: {}".format(mx_digits))