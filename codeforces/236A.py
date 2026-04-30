# If the number of distinc characters is odd is male, otherwise is a female

# Input: wjmzbmr Output: "CHAT WITH HER!"
# Input: xiaodao Output: "IGNORE HIM!"
# Input: sevenkplus Output: "CHAT WITH HER!"

string: str = str(input())

characters: set = set()

for i in range(len(string)):
  characters.add(string[i])

if len(characters) % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
