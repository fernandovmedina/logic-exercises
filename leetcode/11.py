class Solution:
    def maxArea(self, height: list[int]) -> int:
      left = 0
      right = len(height) - 1
      max_area = 0

      while left < right:
        h = min(height[left], height[right])
        w = right - left

        max_area = max(max_area, h * w)

        if height[left] < height[right]:
          left += 1
        else:
          right -= 1

      return max_area

x = Solution()

print(x.maxArea(height = [1,8,6,2,5,4,8,3,7])) # Output: 49
print(x.maxArea(height = [1,1])) # Output: 1
