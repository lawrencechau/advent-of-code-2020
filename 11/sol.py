from copy import deepcopy
from pprint import pprint

#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))
dat = open('input').read().strip().split('\n')
#dat = open('example').read().strip().split('\n')
dat = [list(s) for s in dat]
m = len(dat)
n = len(dat[0])

def adjacent(curr, i, j):
  rs = max(0, i-1)
  cs = max(0, j-1)
  re = min(i+2, m)
  ce = min(j+2, n)
  res = 0
  for r in range(rs, re):
    for c in range(cs, ce):
      if not (r == i and c == j) and curr[r][c] == '#':
        res += 1
  return res

def check_diagonal(curr, i, j, ):

def adjacent2(curr, i, j):
  rs = max(0, i-1)
  cs = max(0, j-1)
  re = min(i+2, m)
  ce = min(j+2, n)
  res = 0
  
  # top
  r = i
  while r > 0 and curr[r][j] == '.':
    r -= 1
  res += 1 if curr[r][j] == '#' else 0


  # down
  r = i
  while r < m-1 and curr[r][j] == '.':
    r -= 1
  res += 1 if curr[r][j] == '#' else 0

  # left
  c = j
  while c > 0 and curr[i][c] == '.':
    c -= 1
  res += 1 if curr[i][c] == '#' else 0

  # right
  c = j
  while c < n-1  and curr[i][c] == '.':
    c += 1
  res += 1 if curr[i][c] == '#' else 0

  # upper left diag
  r, c = max(0, i-1), max(0, j-1)
  for row in range(i

  # upper right diag

  # lower left diag

  # lower right diag

  return res

def next_round(curr):
  res = deepcopy(curr)
  for r in range(m):
    for c in range(n):
      if curr[r][c] == '.':
        continue
      adj = adjacent(curr, r, c)
      if curr[r][c] == 'L' and not adj:
        res[r][c] = '#'
      elif curr[r][c] == '#' and adj >= 4:
        res[r][c] = 'L'
  return res

def next_round2(curr):
  res = deepcopy(curr)
  for r in range(m):
    for c in range(n):
      if curr[r][c] == '.':
        continue
      adj = adjacent2(curr, r, c)
      if curr[r][c] == 'L' and not adj:
        res[r][c] = '#'
      elif curr[r][c] == '#' and adj >= 5:
        res[r][c] = 'L'
  return res

def part1():
  i = 0
  prev = []
  curr = dat
  while prev != curr:
    i += 1
    prev = deepcopy(curr)
    curr = next_round(curr)
    # print(i)
    # pprint(prev)
    # pprint(curr)
    # print('---')

  print(sum(1 for r in range(m) for c in range(n) if curr[r][c] == '#'))

def part2():
  i = 0
  prev = []
  curr = dat
  while prev != curr:
    i += 1
    prev = deepcopy(curr)
    curr = next_round2(curr)
    # print(i)
    # pprint(prev)
    # pprint(curr)
    # print('---')

  print(sum(1 for r in range(m) for c in range(n) if curr[r][c] == '#'))

part1()
part2()
