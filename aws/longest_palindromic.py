# Dado un string s, devuelve el palíndromo más largo.
s = "babad"

# Output: "aba" || "bab"

def isPalindrome(x: str) -> bool:
  return (x)[::-1] == x

def longestPalindrome(s: str) -> str:
  x = 0
  longest_palindrome = ""
  for i in range(len(s)):
    for j in range(i, len(s)):
      substring = s[i : j + 1]
      if isPalindrome(substring):
        if len(substring) > x:
          longest_palindrome = substring
          x = len(substring)
  return longest_palindrome

print(longestPalindrome(s))
