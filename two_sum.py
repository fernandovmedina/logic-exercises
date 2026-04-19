arr = [2,7,11,15]
target = 9

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    list: list[int] = []
    for i in range(len(nums)):
      for j in range(len(nums)):
        if i == j:
          continue
        else:
          if nums[i] + nums[j] == target:
            if [j,i] in list:
              continue
            list.append(i)
    return list

x = Solution()

print(x.twoSum(arr, target))