# Link: https://leetcode.com/problems/special-array-ii/description/?envType=daily-question&envId=2024-12-09

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        d = {0: 0}
        count = 0
        ans = []

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                count += 1

            d[i] = count

        for start, end in queries:
            if d[start] == d[end]:
                ans.append(True)
            else:
                ans.append(False)

        return ans