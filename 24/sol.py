import math
from collections import defaultdict, deque

dat = open('example').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')

d = {}
directions = {'e': (1,1,0),'se': (1,0,-1),'sw': (0,-1,-1),'w': (-1,-1,0),'nw': (-1,0,1),'ne': (0,1,1)}

class Tile:
  def __init__(self, x=0, y=0, z=0):
    self.coords = (x, y, z)
    self.black = False

  def move(self, dir):
    target = [0] * len(self.coords)
    for i in range(len(self.coords)):
      target[i] = self.coords[i] + directions[dir][i]
    target = tuple(target)
    if target in d:
      return d[target]
    else:
      tile = Tile(*target)
      d[tile.coords] = tile
      return tile 

  def can_flip(self):
    blacks = 0
    for direction in directions.keys():
      blacks += self.move(direction).black
    if self.black and (blacks == 0 or blacks > 2):
      return True
    elif not self.black and blacks == 2:
      return True
    else:
      return False
      

def get_directions(line):
  res = []
  i = 0
  while i < len(line):
    direction = line[i]
    i += 1
    if direction in 'ns':
      direction += line[i]
      i += 1
    res.append(direction)
  return res

start = Tile()
d[(0,0,0)] = start

#line = "esew"
#line = "nwwswee"

for line in dat:
  curr = start
  for direction in get_directions(line):
    curr = curr.move(direction)
  curr.black = not curr.black
    #print(f'{direction} - {curr.coords}')
print(sum(tile.black for tile in d.values()))

for i in range(100):
  flip = []
  for tile in list(d.values()):
    if tile.can_flip():
      flip.append(tile.coords)
  for coord in flip:
    d[coord].black = not d[coord].black
  print(f'Day {i+1}: {sum(tile.black for tile in d.values())}')
