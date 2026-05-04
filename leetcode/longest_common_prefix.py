class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    for i in range(len(strs[0])):
      for s in strs:
        if i >= len(s) or s[i] != strs[0][i]:
          return strs[0][:i]
    
    return strs[0]

x = Solution()

print(x.longestCommonPrefix(["flower","flow","flight"]))
print(x.longestCommonPrefix(["dog","racecar","car"]))
