class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
      return []
    
    letters: dict = {}
    letters["2"] = "abc"
    letters["3"] = "def"
    letters["4"] = "ghi"
    letters["5"] = "jkl"
    letters["6"] = "mno"
    letters["7"] = "pqrs"
    letters["8"] = "tuv"
    letters["9"] = "wxyz"

    d: list[str] = [str(d) for d in digits]

    combinations: list[list[str]] = []

    for i in range(len(d)):
      combinations.append([str(dy) for dy in str(letters[d[i]])])

    f: list[str] = combinations[0]

    for i in range(1, len(combinations)):
      temp: list[str] = []
      for l1 in f:
        for l2 in combinations[i]:
          temp.append(l1 + l2)
      f = temp

    return f

x: Solution = Solution()

print(x.letterCombinations("23")) # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# x.letterCombinations("2")  # Output: ["a","b","c"]
