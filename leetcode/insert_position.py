class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    if target in nums:
      return nums.index(target)
    else:
      for i in range(len(nums)):
        if nums[i] > target:
          return i
        elif i == len(nums) - 1:
          return len(nums)
    
x = Solution()

nums = [1,3,5,6]
target = 5

nums2 = [1,3,5,6]
target2 = 2

nums3 = [1,3,5,6]
target3 = 7

print(x.searchInsert(nums, target)) # Output: 2
print(x.searchInsert(nums2, target2)) # Output: 1
print(x.searchInsert(nums3, target3)) # Output: 4
