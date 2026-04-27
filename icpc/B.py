import math

class Solution:
  def isLog10(self, n: int) -> bool:
    return n > 0 and math.log10(n).is_integer()
  
  def formatLog10(self, n: int) -> str:
    return f"10^{len(str(n)) - 1}"
  
  def formatCNotation(self, n: int) -> str:
    ss = str(n)
    ss_clean = ss.rstrip('0')
    exponente = len(ss) - 1
    if len(ss_clean) == 1:
      return f"{ss_clean}\\cdot10^{{{exponente}}}"
    mantisa = ss_clean[0] + "." + ss_clean[1:]
    return f"{mantisa}\\cdot10^{{{exponente}}}"
  
  def Latex(self, string: str) -> str:
    lines: list[str] = string.splitlines()
    numbers: list[int] = []
    temp_n: str = ""
    c: bool = False
    for i in range(len(lines)):
      for j in range(len(lines[i])):
        if lines[i][j].isdecimal():
          temp_n += lines[i][j]
          c = True
        elif not lines[i][j].isdecimal():
          if c:
            numbers.append(int(temp_n))
            temp_n = ""
          c = False
    if temp_n:
      numbers.append(int(temp_n))
    nn: list[str] = []
    for i in range(len(numbers)):
      if self.isLog10(numbers[i]):
        nn.append(self.formatLog10(numbers[i]))
      else:
        nn.append(self.formatCNotation(numbers[i]))
    print(nn)
    print(numbers)

string: str = """This example shows a value
Of 1000000000 without being compressed to 10^{9}
Which is annoying when read. $ S_{10} = 2^{100000} + 780000 $
My ID is RA180000 but that was back in the year 20000"""

x = Solution()

print(x.Latex(string))
