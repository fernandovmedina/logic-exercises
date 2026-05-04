class Solution:
  def romanToInt(self, s: str) -> int:
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    total = 0
    
    if self.verifyNoMoreThanThree(s):
      return -1

    i = 0
    
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
    
    if i < len(s):
      total += dictionary[s[i]]
    return total

  
  def verifyNoMoreThanThree(self, s: str) -> bool:
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            if count > 3:
                return True
        else:
            count = 1
    return False

x = Solution()

print(x.romanToInt("III")) # 3
print(x.romanToInt("LVIII")) # 58
print(x.romanToInt("MCMXCIV")) #1994
print(x.romanToInt("MDCCCLXXXIV")) # 1884
print(x.romanToInt("MMMCMXCIX")) # 3999
    