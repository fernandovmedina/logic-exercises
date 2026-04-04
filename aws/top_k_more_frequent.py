# Dado un arreglo nums y un entero k, devuelve los k elementos más frecuentes.
nums = [1,1,1,2,2,3]
k = 2

# Ouput: [1,2]

def top_k_frequent(nums: list[int], k: int) -> list[int]:
  freq_map = {}

  for num in nums:
    if num in freq_map:
      freq_map[num] += 1
    else:
      freq_map[num] = 1

  sorted_nums = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

  result = []
  for i in range(k):
    result.append(sorted_nums[i][0])

  return result

print(top_k_frequent(nums, k))