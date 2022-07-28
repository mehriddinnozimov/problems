# berilgan qiymatdan kichik qiymatlarni oldinga o`tqazuvchi linked list

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

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


class Solution:
    def partition(self, head, x):
      array = parseListNode(head)
      array.sort(key= lambda a: a >= x)
      return toListNode(array)

s = Solution()
print(parseListNode(s.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)))


print(parseListNode(s.partition(ListNode(2, ListNode(1)), 2)))