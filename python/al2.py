# 2 list Nodeni teskarisiga qo`shish
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self):
  	return f"Value: {self.val}, Next: {self.next}"

def list_to_string(listNode):
	temp = listNode
	value = ""
	while not (temp is None):
		value = str(temp.val) + value
		temp = temp.next
	return value


node1 = ListNode(2, ListNode(4, ListNode(3)))
node2 = ListNode(5, ListNode(6, ListNode(4)))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    	v1 = list_to_string(l1)
    	v2 = list_to_string(l2)
    	value = str(int(v1) + int(v2))[::-1]
    	returnedValue = ListNode(int(value[0:1]), None)
    	temp = returnedValue
    	for el in value[1:]:
    		temp.next = ListNode(int(el), None)
    		temp = temp.next
    			
    	return returnedValue

s = Solution()
print(s.addTwoNumbers(node1, node2))

