class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    arr: list[str] = s.split()
    return len(arr[len(arr) - 1])

x = Solution()

s1 = "Hello World"
print(x.lengthOfLastWord(s1)) # Output: 5

s2 = "   fly me   to   the moon  "
print(x.lengthOfLastWord(s2)) # Output: 4

s3 = "luffy is still joyboy"
print(x.lengthOfLastWord(s3)) # Output: 6
