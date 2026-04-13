class Solution:
  def minimumTemperature(self, numberOfCleanDays: int, numberOfHolidays: int, temperatures: list[int]) -> int:
    i: int = 1
    tmprs: list[int] = []
    while i < len(temperatures) and i < numberOfHolidays:
      if i == 0:
        tmprs.append(temperatures[i + numberOfCleanDays])
        i += 2
      elif i > 0:
        tmprs.append(temperatures[i + numberOfCleanDays])
        i += 3
      elif i == len(temperatures) or i > len(temperatures):
        break
    return max(tmprs)
    
x = Solution()

numberOfCleanDays = 2
numberOfHolidays = 6
temperatures = [-20, -10, -5, -10, -2, -40]

print(x.minimumTemperature(numberOfCleanDays, numberOfHolidays, temperatures))
