class Solution:
  def returnCenters(self, arr: list[int]) -> list[int]:
    if len(arr) % 2 == 1:
      return [arr[int(len(arr) / 2)]]
    else:
      return [arr[int((len(arr) / 2) - 1)], arr[int(len(arr) / 2)]]
  
  def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    newList: list[int] = nums1 + nums2
    newList.sort()
    
    mid: list[int] = self.returnCenters(newList)
    
    if len(mid) == 1:
      return float(f"{mid[0]:.5f}")
    else:
      return float(f"{(sum(mid) / 2):.5f}")
    
x = Solution()

print(x.findMedianSortedArrays([1,3], [2]))
print(x.findMedianSortedArrays([1,2], [3,4]))
