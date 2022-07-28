# tartibni buzmasdan hosil qila olish mumkin bo`lgan so`zlarning sonini aniqlash

class Solution:
  def numMatchingSubseq(self, s, ws):
    n = len(ws)
    for w in ws:
      t = s
      for l in w:
        try:
          i = t.index(l)
          t =  t[i+1:]
        except:
          n -= 1
          break
    return n