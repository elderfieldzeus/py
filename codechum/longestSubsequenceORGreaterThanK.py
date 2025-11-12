arr = list(map(int, input("Enter elements: ").split()))

k = int(input("Enter k: "))

mx = 0

for i in range(len(arr)):
    ans = 0
    for j in range(i, len(arr)):
        ans |= arr[j]
        
        if ans <= k:
            mx = max(mx, j - i + 1)
        else:
            break
            
print("The longest subsequence with OR under k is of size: {}".format(mx))