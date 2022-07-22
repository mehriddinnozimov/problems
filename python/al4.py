# paskal uchburchagi

class Solution:
  def generate(self, numRows):
    rl = [[] for x in range(numRows+1)]
    for i in range(numRows+1):
      for y in range(i):
        if y == 0 or y + 1 == i:
          rl[i].append(1)
        else:
          rl[i].append(rl[i-1][y-1] + rl[i-1][y])
    rl.pop(0)
    return rl


s = Solution()
print(s.generate(5))