class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    temp: int = float("inf")
    for i in range(len(nums)):
      