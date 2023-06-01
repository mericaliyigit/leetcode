from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]

        def checker(j):
            if j < 0 or j >= len(pascal[-1]):
                return 0
            else:
                return pascal[-1][j]

        for i in range(numRows - 1):
            row = []
            for j in range(-1, len(pascal[-1])):
                num = checker(j) + checker(j+1)
                row.append(num)
            pascal.append(row)
        return pascal


numRows = 5
solution = Solution()
res = solution.generate(numRows)
print(res)
