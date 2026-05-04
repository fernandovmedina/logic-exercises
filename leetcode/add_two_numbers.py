from typing import Optional

class Solution:
  def buildListNode(self, arr: list[int]) -> ListNode:
    dummy = ListNode()
    current = dummy
    
    for num in arr:
      current.next = ListNode(num)
      current = current.next
      
    return dummy.next
    
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    arr1 = []
    arr2 = []
    
    current = l1
    while current:
      arr1.append(current.val)
      current = current.next
    
    current = l2
    while current:
      arr2.append(current.val)
      current = current.next
      
    arr1.reverse()
    arr2.reverse()
    
    num1 = int(''.join(map(str, arr1)))
    num2 = int(''.join(map(str, arr2)))
    
    value = num1 + num2
    
    arrValue = [int(d) for d in str(value)]
    
    return self.buildListNode(arrValue[::-1])

x = Solution()

print(x.addTwoNumbers(l1=[2,4,3], l2=[5,6,4])) # Output: [7,0,8]
print(x.addTwoNumbers(l1=[0], l2=[0])) # Output: [0]
print(x.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9])) # Output: [8,9,9,9,0,0,0,1]
