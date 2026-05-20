# If the number of distinc characters is odd is male, otherwise is a female

# Input: wjmzbmr Output: "CHAT WITH HER!"
# Input: xiaodao Output: "IGNORE HIM!"
# Input: sevenkplus Output: "CHAT WITH HER!"

string: str = str(input())

characters: set = set()

for i in range(len(string)):
  characters.add(string[i])

print((lambda x: "CHAT WITH HER!" if x % 2 == 0 else "IGNORE HIM!")(len(characters)))
