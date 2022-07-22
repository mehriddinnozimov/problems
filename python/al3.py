# zigzag konveyter

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    list_s = []
    temp0 = numRows - 2
    if temp0 < 0:
      temp0 = 0
    list_s.append([x for x in s[0:numRows]])
    skip = 0
    for (i, ch) in enumerate(s[numRows:]):
      if skip == 0:
        if temp0 != 0:
          list1 = ["" for i in range(numRows)]
          list1[temp0] = ch
          list_s.append(list1)
          temp0 -= 1

        else:
          list_s.append([x for x in s[numRows+i:numRows+i+numRows]])
          temp0 = numRows - 2
          skip = numRows - 1
      else:
        skip -= 1
        continue
      if temp0 < 0:
        temp0 = 0
    v = ""
    for r in range(numRows):
      v+= "".join([el[r] for el in list_s if len(el) > r])
    return v

s = Solution()
print(s.convert("PAYPALISHIRING", 4))