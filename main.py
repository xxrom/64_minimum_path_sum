from typing import List, Dict
import sys


class Solution:

  def bfs(self) -> int:
    # print('--------------------------------')
    print('stack', self.stack)
    # print('minDistMap', self.minDistMap)
    # print('checkMap', self.checkMap)
    if len(self.stack) == 0:
      # print('end =)')
      return 0

    # get first element coordinates from stack
    i, j = self.stack.pop(0)
    # print('%d / %d' % (i, j))

    bottomPosition = sys.maxsize
    rightPosition = sys.maxsize

    if i + 1 < self.iSize:
      bottomPosition = self.minDistMap[i + 1][j]
    if j + 1 < self.jSize:
      rightPosition = self.minDistMap[i][j + 1]

    currentMin = min(bottomPosition, rightPosition)
    if currentMin == sys.maxsize:
      currentMin = 0

    self.minDistMap[i][j] += currentMin

    if i - 1 >= 0 and self.checkMap[i - 1][j] != True:
      self.checkMap[i - 1][j] = True
      self.stack.append([i - 1, j])
      # print('added i -1 ', self.stack)

    if j - 1 >= 0 and self.checkMap[i][j - 1] != True:
      self.checkMap[i][j - 1] = True
      self.stack.append([i, j - 1])
      # print('added j -1', self.stack)

    self.bfs()

  def minPathSum(self, grid: List[List[int]]) -> int:
    '''
    # Problem with coping grid list to new checkMap ...
    checkMap = grid[:]

    for i in range(len(checkMap)):
      for j in range(len(checkMap[0])):
        checkMap[i][j] = False
    '''

    self.iSize = len(grid)
    self.jSize = len(grid[0])

    self.checkMap = []
    for i in range(self.iSize):
      self.checkMap.append([])
      for j in range(self.jSize):
        self.checkMap[i].append(False)

    # print('self.checkMap', self.checkMap)

    self.minDistMap = grid
    self.stack = [[self.iSize - 1, self.jSize - 1]]
    self.bfs()
    # print(minDistMap)

    # TODO: find path from the end to start, get min value and that all !!!
    return self.minDistMap[0][0]


my = Solution()
n = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# TODO: find path from the end to start, get min value and that's all !!!
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
'''
# from end to start, on each step get sum = min(prevBottom, prevRight) + currentStep
# for Each step
n = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
n = [
  [7, 6, 3],
  [8, 7, 2],
  [7, 3, 1]
]
'''

# Runtime: 152 ms, faster than 26.33% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 49.2 MB, less than 5.26% of Python3 online submissions for Minimum Path Sum.
'''
Fast solution (optimized solution =) )
URL: https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms

def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
'''