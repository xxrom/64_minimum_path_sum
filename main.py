from typing import List, Dict
import sys


class Solution:

  def bfs(self, i: int, j: int, pathObj: Dict[str, bool]) -> int:
    if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
      # print('END!')
      # pathSum = sum(pathObj.values()) + self.grid[i][j]
      # print('path sum ', pathSum, pathObj)
      return sum(pathObj.values())

    bottomPathSum = sys.maxsize
    rightPathSum = sys.maxsize

    if i + 1 < len(self.grid):
      bottomPathObj = pathObj.copy()
      bottomPathObj[str(i + 1) + ',' + str(j)] = self.grid[i + 1][j]
      bottomPathSum = self.bfs(i + 1, j, bottomPathObj)

    if j + 1 < len(self.grid[0]):
      rightPathObj = pathObj.copy()
      rightPathObj[str(i) + ',' + str(j + 1)] = self.grid[i][j + 1]
      rightPathSum = self.bfs(i, j + 1, rightPathObj)

    return bottomPathSum if rightPathSum > bottomPathSum else rightPathSum

  def minPathSum(self, grid: List[List[int]]) -> int:
    self.grid = grid
    # TODO: find path from the end to start, get min value and that all !!!
    return self.bfs(0, 0, {'0,0': grid[0][0]})


my = Solution()
n = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# TODO: find path from the end to start, get min value and that all !!!
# TOO SLOW !!! =)))))
# n = [[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
#      [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
#      [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
#      [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
#      [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
#      [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
#      [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
#      [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
#      [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
#      [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
#      [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
#      [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
ans = my.minPathSum(n)
print("ans", ans)