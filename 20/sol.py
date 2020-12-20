import math
from collections import defaultdict
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('ex').read().strip().split('\n')))

#dat = open('example').read().strip().split('\n')
dat = open('example').read().strip().split('\n\n')
#dat = open('input').read().strip().split('\n')

m = len(dat)

class Tile:
  def __init__(self, block, tid='', top='', right='', bottom='', left=''):
    if block:
      self.id = int(block[0].split()[1][:-1])

      self.top = set()
      for c in range(0,10):
        if block[1][c] == '#':
          self.top.add(c)

      self.right = set()
      for r in range(1,11):
        if block[r][-1] == '#':
          self.right.add(r-1)
   
      self.bottom = set() 
      for c in range(0,10):
        if block[-1][c] == '#':
          self.bottom.add(c)

      self.left = set()
      for r in range(1,11):
        if block[r][0] == '#':
          self.left.add(r-1)
    else:
      self.id = tid
      self.top = top
      self.right = right
      self.bottom = bottom
      self.left = left
 
  def flip(self):
    return Tile(None,self.id, self.bottom, self.left, self.top, self.right)

  def rotate(self):
    return Tile(None,self.id, self.left, self.top, self.right, self.bottom)

dat = [Tile(b.split('\n')) for b in dat]
for t in dat:
  print(f"==={t.id}===")
  print(t.top)
  print(t.right)
  print(t.bottom)
  print(t.right)

def build(tiles, t_idx, r, c, res):
  print(t_idx, r, c)
  for t in range(t_idx, len(tiles)):
    tiles[t_idx], tiles[t] = tiles[t], tiles[t_idx]
    res[r][c] = tiles[t_idx]
    nc = (c+1) % 3
    nr = r+1 if nc == 0 else r
    for _ in range(4):
      for _ in range(2):
        if c > 1:
          if res[r][c-1].right != res[r][c].left:
            continue
        if r > 1:
          if res[r-1][c].bottom != res[r][c].top:
            continue
        if build(tiles, t_idx+1, nr, nc, res):
          return True
        res[r][c] = res[r][c].flip()
      res[r][c] = res[r][c].rotate()
    tiles[t_idx], tiles[t] = tiles[t], tiles[t_idx]
  return False

res = [[None for _ in range(3)] for _ in range(3)]
#build(dat,0, 0, 0, res)
print(math.prod([res[0][0].id, res[0][-1].id, res[-1][0].id, res[-1][-1]]))
