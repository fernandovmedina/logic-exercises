class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
      return s

    rows = [""] * numRows
    i = 0
    step = 1

    for c in s:
      rows[i] += c

      if i == 0:
        step = 1
      elif i == numRows - 1:
        step = -1

      i += step

    return "".join(rows)

x = Solution()

print(x.convert("PAYPALISHIRING", 3)) # Output: "PAHNAPLSIIGYIR"
print(x.convert("PAYPALISHIRING", 4)) # Output: "PINALSIGYAHRPI"
