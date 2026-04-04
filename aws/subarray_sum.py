# Dado un arreglo nums y un entero k, devuelve el número de subarrays que suman k.
nums = [1,1,1,2,3,1,1,1,2,3]
k = 2

# Output: 2

def sub_array_sum(nums: list[int], k: int) -> int:
  count: int = 0
  arrays: list[int] = []
  for i in range(len(nums) - 1):
    arrays.append([nums[i], nums[i + 1]])
  for array in arrays:
    if sum(array) == k:
      count += 1
  return count

print(sub_array_sum(nums, k))
