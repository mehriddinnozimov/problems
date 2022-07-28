def parseListNode(node):
  temp = node 
  array = []
  while temp is not None:
    array.append(temp.val)
    temp = temp.next
  return array

def toListNode(array):
  linked = None
  temp = None
  for el in array:
    if(linked is None):
      linked = ListNode(el)
      temp = linked
    else:
      temp.next = ListNode(el)
      temp = temp.next
  return linked

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
      arr = parseListNode(node)
      new_arr = []
      reverse_arr = []
      for (index, el) in enumerate(arr):
        if index < left -1:
          new_arr.append(el)
        elif index > right -1:
          new_arr.append(el)
        else:
          new_arr.append(" ")
          reverse_arr.insert(0, el)
      for (index, el) in enumerate(reverse_arr):
        new_arr[index+left-1] = el
      return toListNode(new_arr)


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
print(s.reverseBetween(node, 2, 4))