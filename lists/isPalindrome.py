def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True

name = input("Enter a string: ")

print("Yes" if isPalindrome(name) else "No")