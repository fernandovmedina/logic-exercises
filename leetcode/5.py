class Solution:
  def isPalindrome(self, x: str) -> bool:
    return x[::-1] == x

  def longestPalindrome(self, s: str) -> str:
    p: list[str] = []

    for i in range(len(s)):
      sr: str = s[i]

      p.append(sr)

      for j in range(i + 1, len(s)):
        sr += s[j]

        if self.isPalindrome(sr):
          p.append(sr)

    return max(p, key=len)

print(Solution().longestPalindrome("babad")) # Output: "aba" or "bab"
print(Solution().longestPalindrome("cbbd"))  # Output: "bb"
print(Solution().longestPalindrome("a"))     # Output: "a"
print(Solution().longestPalindrome("ac"))    # Output: "a"
