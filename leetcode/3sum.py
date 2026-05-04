class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = set()

    for i in range(len(nums)):
      seen = set()
      
      for j in range(i + 1, len(nums)):
        complemento = -(nums[i] + nums[j])

        if complemento in seen:
          tripleta = tuple(sorted([nums[i], nums[j], complemento]))
          res.add(tripleta)

        seen.add(nums[j])

    return [list(t) for t in res]

x = Solution()

nums = [-1,0,1,2,-1,-4]
print(x.threeSum(nums)) # Output: [[-1,-1,2],[-1,0,1]]

print("======================================")

nums = [0,1,1]
print(x.threeSum(nums)) # Output: []

print("======================================")

nums = [0,0,0]
print(x.threeSum(nums)) # Output: [[0,0,0]]
