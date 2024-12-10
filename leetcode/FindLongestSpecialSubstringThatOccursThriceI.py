# Link: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/?envType=daily-question&envId=2024-12-10

class Solution:
    def maximumLength(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            lst = []
            
            for j in range(len(s) - i + 1):
                x = s[j: j + i]
                if len(set(x)) == 1:
                    lst.append(x)

            if any([lst.count(x) >= 3 for x in lst]):
                return i

        return -1
