import math

def binary_search(arr, target):
	low = 0 
	hight = len(arr)
	if arr[len(arr) -1] < target or arr[0] > target:
		return -1

	while low <= hight:
		middle = math.ceil(low + (hight - low) // 2)
		if(target == arr[middle]):
			return middle
		elif (target < arr[middle]):
			hight = middle - 1
		else:
			low = middle + 1
	return -1

class Solution:
  def searchMatrix(self, matrix, target):
  	for arr in matrix:
  		result = binary_search(arr, target)
  		if result > -1: 
  			return True
  	return False


matrix = [
 	[1,4,7,11,15],
 	[2,5,8,12,19],
 	[3,6,9,16,22],
 	[10,13,14,17,24],
 	[18,21,23,26,30]
]

s = Solution()
print(s.searchMatrix(matrix, 20))