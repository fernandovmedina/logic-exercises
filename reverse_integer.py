class Solution:
  def reverse(self, x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)

    arr: list[int] = [int(d) for d in str(x)]
    newArr: list[int] = arr[::-1]

    string: str = ""
    for i in range(len(newArr)):
      string += str(newArr[i])

    result = int(string) * sign

    if result < -2**31 or result > 2**31 - 1:
      return 0

    return result

x = Solution()

print(x.reverse(123)) # Output: 321
print(x.reverse(-123)) # Output: -321
print(x.reverse(120)) # Output: 21
print(x.reverse(1534236469)) # Output: 0
