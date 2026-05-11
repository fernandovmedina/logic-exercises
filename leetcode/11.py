class Solution:
  def maxArea(self, height: list[int]) -> int:
    tmp1: int = 0
    tmp2: int = -999
    for i in range(len(height)):
      if height[i] > tmp1:
        tmp1 = height[i]
    for i in range(len(height)):
      if height[i] > tmp2 and height[i] < tmp1:
        tmp2 = height[i]
    if tmp2 == -999:
      tmp2 = tmp1
    return tmp2 * tmp2

x = Solution()

x.maxArea(height = [1,8,6,2,5,4,8,3,7]) # Output: 56
x.maxArea(height = [1,1]) # Output: 1
