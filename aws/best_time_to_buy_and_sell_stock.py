prices = [7,1,5,3,6,4]

# Output: 5

def max_profit(prices: list[int]) -> int:
  profits: list[int] = []
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      profits.append(prices[j] - prices[i])
  return max(profits)

print(max_profit(prices))