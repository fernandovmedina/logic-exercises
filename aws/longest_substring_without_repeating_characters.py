s: str = "abcabcdeabb"

def longest_substring(s: str) -> int:
  letters = []
  counts: list[int] = []
  for char in s:
    if char not in letters:
      letters.append(char)
    else:
      counts.append(len(letters))
      letters.clear()
  return max(counts)

print(longest_substring(s))
