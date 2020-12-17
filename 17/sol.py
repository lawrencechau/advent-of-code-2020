from collections import defaultdict
# int
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))

 
#dat = open('example').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')
dat = open('input').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')

m = len(dat)
n = len(dat[0])

d = defaultdict(int)

def neighbors(x,y,z,w=0):
  res = []
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      for k in range(z-1, z+2):
        for l in range(w-1, w+2):
          if (i,j,k,l) != (x,y,z,w):
            yield (i,j,k,l)

active = set()
points = defaultdict(int)
for r in range(m):
  for c in range(n):
    if dat[r][c] == '#':
      active.add((r,c,0,0))

cycles = 6
for i in range(cycles):
  n_points = defaultdict(int)
  for ax, ay, az, aw in active:
    for nei in neighbors(ax, ay, az, aw):
      n_points[nei] += 1
  n_active = set()
  for p, count in n_points.items():
    if p in active and count in (2,3):
      n_active.add(p)
    elif p not in active and count == 3:
      n_active.add(p)
  active = n_active

print(len(active))
