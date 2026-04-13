class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    k: int = 0
    duplicates: list[int] = []
    for i in range(len(nums) - 1):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
          duplicates.append(nums[j])
          k += 1
          break
    return k
    
x = Solution()

nums: list[int] = [1,1,2]
nums2: list[int] = [0,0,1,1,1,2,2,3,3]

print(x.removeDuplicates(nums))  # Output => 2
print(x.removeDuplicates(nums2)) # Output => 5
