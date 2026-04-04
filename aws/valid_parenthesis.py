s = "()[]{}"
string_max = "(([]))"

def is_valid(s: str) -> bool:
  stack = []
  mapping = {")": "(", "]": "[", "}": "{"}

  for char in s:
    if char in mapping.values():
      stack.append(char)
    elif char in mapping.keys():
      if not stack or stack.pop() != mapping[char]:
        return False

  return not stack

print(is_valid(s))
print(is_valid(string_max))