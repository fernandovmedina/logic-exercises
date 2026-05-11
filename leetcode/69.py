class Solution:
  def mySqrt(self, x: int) -> int:
    return int(x ** 1/2)

import sys

input = sys.stdin.readline

number = int(input().strip())

print(Solution().mySqrt(number))
