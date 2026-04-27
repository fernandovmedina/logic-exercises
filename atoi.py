class Solution:
  def myAtoi(self, s: str) -> int:
    s: str = s.lstrip()
    
    if not s:
      return 0

    f: str = ""
    sign: int = 1
    i: int = 0

    if s[0] == "-":
      sign = -1
      i += 1
    elif s[0] == "+":
      i += 1

    while i < len(s) and s[i].isdigit():
      f += s[i]
      i += 1

    if f == "":
      return 0

    num = int(f) * sign

    INT_MIN: int = -2**31
    INT_MAX: int = 2**31 - 1

    if num < INT_MIN:
      return INT_MIN
    if num > INT_MAX:
      return INT_MAX

    return num

x = Solution()

print(x.myAtoi("42")) # Output: 42
print(x.myAtoi("-042")) # Output: -42
print(x.myAtoi("1337c0d3")) # Output: 1337
print(x.myAtoi("0-1")) # Output: 0
print(x.myAtoi("   -042")) # Output: -42
print(x.myAtoi("words and 987")) # Output: 
print(x.myAtoi("-91283472332")) # Output: -2147483648
