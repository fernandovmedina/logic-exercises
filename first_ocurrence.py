class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
      return haystack.find(needle)
    else:
      return -1

x = Solution()

haystack = "sadbutsad"
needle = "sad"

haystack2 = "leetcode"
needle2 = "leeto"

print(x.strStr(haystack, needle)) #Output: 0
print(x.strStr(haystack2, needle2)) #Output: -1
