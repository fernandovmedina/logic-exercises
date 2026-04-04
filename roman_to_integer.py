class Solution:
  def romanToInt(self, s: str) -> int:
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # Here we store the value of the roman numeral
    total = 0
    # First we check that one of the letters in the string does not repite more than 3 times in a row
    if self.verifyNoMoreThanThree(s):
      return -1
    # Init the index
    i = 0
    # We iterate through the string
    while i < len(s) - 1:
      if dictionary[s[i]] > dictionary[s[i + 1]]:
        total += dictionary[s[i]]
        i += 1
      elif dictionary[s[i]] < dictionary[s[i + 1]]:
        total += dictionary[s[i + 1]] - dictionary[s[i]]
        i += 2
      else:
        total += dictionary[s[i]]
        i += 1
    # Here we add the last value of the string
    if i < len(s):
      total += dictionary[s[i]]
    return total

  # Function to verify that the same letter does not repit more than 3 times
  def verifyNoMoreThanThree(self, s: str) -> bool:
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            if count > 3:
                return True
        else:
            count = 1  # ← reiniciar al cambiar de letra
    return False

x = Solution()

print(x.romanToInt("III"))
print(x.romanToInt("LVIII"))
print(x.romanToInt("MCMXCIV"))
print(x.romanToInt("MDCCCLXXXIV"))
    