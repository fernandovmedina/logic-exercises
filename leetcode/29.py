class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    if dividend == INT_MIN and divisor == -1:
      return INT_MAX

    return int(dividend / divisor)
  
print(Solution().divide(-2147483648, -1))
