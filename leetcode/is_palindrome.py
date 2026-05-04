class Solution:
  def isPalindrome(self, x: int) -> bool:
    return str(x)[::-1] == str(x)

x = Solution()

print(x.isPalindrome(-202))