# Link: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2024-12-04

def getPrev(char):
        return chr((ord(char) - ord('a') + 25) % 26 + ord('a'))

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0

        for s in str2:
            prev = getPrev(s)

            while i < len(str1) and str1[i] != s and str1[i] != prev:
                i += 1

            if i == len(str1):
                return False
            else:
                i += 1

        return True 