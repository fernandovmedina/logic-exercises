class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    s: str = ""
    for i in range(len(digits)):
      s += str(digits[i])
    return [int(d) for d in str(int(s) + 1)]
  
x = Solution()

digits1 = [1,2,3]
digits2 = [4,3,2,1]
digits3 = [9]
digits4 = [9,9]

print(x.plusOne(digits1))
print(x.plusOne(digits2))
print(x.plusOne(digits3))
print(x.plusOne(digits4))
