# TIME LIMIT EXCEEDED!!!

# Link: https://leetcode.com/problems/path-with-maximum-probability/?envType=daily-question&envId=2024-12-04

import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visited = set([start_node])
        matrix = [[0] * n for _ in range(n)]
        

        # init matrix
        for i in range(len(edges)):
            matrix[edges[i][0]][edges[i][1]] = succProb[i]
            matrix[edges[i][1]][edges[i][0]] = succProb[i]

        # init probs
        probs = [x for x in matrix[start_node]]

        for i in range(1, n):
            max = -1
            maxIndex = -1

            for index, p in enumerate(probs):
                if index not in visited and p > max:
                    max = p
                    maxIndex = index

            if max != -1:
                visited.add(maxIndex)

                for x in range(n):
                    if x not in visited and probs[x] < probs[maxIndex] * matrix[maxIndex][x]:
                        probs[x] = probs[maxIndex] * matrix[maxIndex][x]


            
            if end_node in visited: # if end_node already found, you can end early
                break

        print(probs)
        return probs[end_node]
