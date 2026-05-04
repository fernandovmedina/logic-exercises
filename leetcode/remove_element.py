class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
      if nums[i] != val:
        nums[k] = nums[i]
        k += 1

    for i in range(k, len(nums)):
      nums[i] = 0
    return k

nums = [3,2,2,3]
val = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

x = Solution()

j = x.removeElement(nums2, val2)
k = x.removeElement(nums, val)

print(k, nums)
print(j, nums2)