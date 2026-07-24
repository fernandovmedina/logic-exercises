class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    if "*" in p:
      characters: list[str] = p.split("*")

      b: list[bool] = []
      if len(characters) > 1:
        for i in range(len(characters)):
          if characters[i] in s:
            b.append(True)
        if True in b:
          return True
      elif len(characters) == 1:
        if characters[0] in s:
          return True
      else:
        if characters[0] == "." and len(s) > 0:
          return True
    else:
      return False

print(Solution().isMatch("aa", "a"))      # Output: false
print(Solution().isMatch("aa", "a*"))     # Output: true
print(Solution().isMatch("ab", ".*"))     # Output: true
print(Solution().isMatch("aab", "c*a*b")) # Output: true
