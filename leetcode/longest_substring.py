class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    lengths: list[int] = []
    
    for i in range(len(s)):
      string = ""
      for j in range(i, len(s)):
        if s[j] in string:
          break
        string += s[j]
      lengths.append(len(string))
    
    return max(lengths) if lengths else 0

x = Solution()

print(x.lengthOfLongestSubstring("abcabcbb")) # Output: 3
print(x.lengthOfLongestSubstring("bbbbb")) # Output: 1
print(x.lengthOfLongestSubstring("pwwkew")) # Output: 3
