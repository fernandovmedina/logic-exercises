class Solution:
  def stringTask(self, line: str) -> str:
    vowels: list[str] = ["A", "O", "Y", "E", "U", "I"]
    nw: str = str.upper(line)
    newline: str = ""
    for i in range(len(nw)):
      if nw[i] in vowels:
        continue
      elif nw[i] not in vowels:
        newline += "." + nw[i]
    return str.lower(newline)
      
x = Solution()

print(x.stringTask("tour"))
print(x.stringTask("Codeforces"))
print(x.stringTask("aBAcAba"))
