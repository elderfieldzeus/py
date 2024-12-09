# Link: https://leetcode.com/problems/move-pieces-to-obtain-a-string/?envType=daily-question&envId=2024-12-05

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        startPair = []
        targetPair = []

        for index, i in enumerate(start):
            if i == 'L' or i == 'R':
                startPair.append((i, index))
        
        for index, i in enumerate(target):
            if i == 'L' or i == 'R':
                targetPair.append((i, index))

        if len(startPair) != len(targetPair):
            return False
        
        for i in range(len(startPair)):
            if (startPair[i][0] != targetPair[i][0]) or (startPair[i][0] == 'L' and startPair[i][1] < targetPair[i][1]) or startPair[i][0] == 'R' and startPair[i][1] > targetPair[i][1]:
                return False

        return True