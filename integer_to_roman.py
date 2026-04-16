class Solution:
  def convertUnitToLetter(self, p: int, u: int) -> str:
    r: str = ""
    match p:
      case 100:
        if u <= 3:
          for i in range(u):
            r += "C"
        match u:
          case 4:
            r += "CD"
          case 5:
            r += "D"
          case 6:
            r += "DC"
          case 7:
            r += "DCC"
          case 8:
            r += "DCCC"
          case 9:
            r += "CM"
      case 10:
        if u <= 3:
          for i in range(u):
            r += "X"
        match u:
          case 4:
            r += "LX"
          case 5:
            r += "L"
          case 6:
            r += "LX"
          case 7:
            r += "LXX"
          case 8:
            r += "LXXX"
          case 9:
            r += "XC"
      case 1:
        if u <= 3:
          for i in range(u):
            r += "I"
        match u:
          case 4:
            r += "IV"
          case 5:
            r += "V"
          case 6:
            r += "VI"
          case 7:
            r += "VII"
          case 8:
            r += "VIII"
          case 9:
            r += "IX"
    return r        
    
  def integerToRoman(self, number: int) -> str:
    roman: str = ""
    
    m: int = int(number / 1000)
    c: int = int((number % 1000) / 100)
    d: int = int(((number % 1000) % 100) / 10)
    u: int = ((number % 1000) % 100) % 10
    
    # Here we just range the thousands bc it can be a maximum of 3
    for i in range(m):
      roman += "M"
    
    roman += self.convertUnitToLetter(100, c)
    roman += self.convertUnitToLetter(10, d)
    roman += self.convertUnitToLetter(1, u)
    
    return roman
  
x = Solution()

numbers = [3, 58, 1994, 1884, 3999]

print([x.integerToRoman(n) for n in numbers])
