class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    temp: int = float("inf")
    k: int = 0
    for i in range(len(nums)):
      if nums[i] != temp:
        temp = nums[i]
        nums[k] = nums[i]
        k += 1
    return k

x = Solution()

nums = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3]
nums3 = [-1,0,0,0,0,3,3]

k1 = x.removeDuplicates(nums)
print(k1, nums[:k1])

k2 = x.removeDuplicates(nums2)
print(k2, nums2[:k2])

k3 = x.removeDuplicates(nums3)
print(k3, nums3[:k3])