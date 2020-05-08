from typing import List, Dict
import sys


class Solution:

  def bfs(self, stack, minDistMap, checkMap) -> int:
    print('--------------------------------')
    print('stack', stack)
    print('minDistMap', minDistMap)
    print('checkMap', checkMap)
    if len(stack) == 0:
      print('end =)')
      return 0

    # get first element coordinates from stack
    i, j = stack.pop(0)
    print('%d / %d' % (i, j))

    bottomPosition = sys.maxsize
    rightPosition = sys.maxsize
    if i + 1 < len(minDistMap):
      bottomPosition = minDistMap[i + 1][j]
    if j + 1 < len(minDistMap[0]):
      rightPosition = minDistMap[i][j + 1]

    currentMin = min(bottomPosition, rightPosition)
    if currentMin == sys.maxsize:
      currentMin = 0

    minDistMap[i][j] += currentMin

    if i - 1 >= 0 and checkMap[i - 1][j] != True:
      checkMap[i - 1][j] = True
      stack.append([i - 1, j])
      print('added i -1 ', stack)

    if j - 1 >= 0 and checkMap[i][j - 1] != True:
      checkMap[i][j - 1] = True
      stack.append([i, j - 1])
      print('added j -1', stack)

    self.bfs(stack, minDistMap, checkMap)

  def minPathSum(self, grid: List[List[int]]) -> int:
    '''
    # Problem with coping grid list to new checkMap ...
    checkMap = grid[:]

    for i in range(len(checkMap)):
      for j in range(len(checkMap[0])):
        checkMap[i][j] = False
    '''

    checkMap = []
    for i in range(len(grid)):
      checkMap.append([])
      for j in range(len(grid[0])):
        checkMap[i].append(False)

    print('checkMap', checkMap)

    minDistMap = grid[:]
    stack = [[len(minDistMap) - 1, len(minDistMap[0]) - 1]]
    self.bfs(stack, minDistMap, checkMap)
    # print(minDistMap)

    # TODO: find path from the end to start, get min value and that all !!!
    return minDistMap[0][0]


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