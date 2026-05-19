class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    if dividend >= -2 ** 31 and dividend <= 2 ** 31 - 1:
      pass

    if dividend == 0:
      return 0
    
    if divisor == 1:
      return dividend
    
    if divisor == -1:
      return -dividend
    
    return int(dividend / divisor)
