import math
from collections import defaultdict, deque

dat = open('example').read().strip()
#dat = open('input').read().strip()

m = len(dat)
#max_rounds = 10
#max_rounds = 100
max_rounds = 10000000 

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

d = {}
#mn, mx = float('inf'), float('-inf')
mn, mx = 1, 1000000 

prev = ph = Node(0)

for idx, digit in enumerate(dat):
  num = int(digit)
  node = Node(num)
  if not idx:
    ph = node
  prev.next = node
  prev = node
  d[num] = node
  mn = min(mn, num)
  mx = max(mx, num)
for num in range(mx+1, 1000001):
  node = Node(num)
  prev.next = node
  prev = node
  d[num] = node

prev.next = ph

def get_dest(num, exclude):
  curr = num-1
  while curr not in d or curr in exclude:
    curr -= 1
    if curr < mn:
      curr = mx
  #print(f'destination: {curr}')
  return d[curr]

def print_ll():
  curr = d[1].next
  s = []
  while curr.val != 1:
    s.append(str(curr.val))
    curr = curr.next
  print(''.join(s))
    
def get_star():
  curr = d[1].next
  print(curr.val * curr.next.val)

curr = ph
for i in range(max_rounds):
  if i % 1000000 == 0:
    print(f'==={i}===')
  start, end = curr.next, curr.next.next.next
  curr.next = end.next
  dest = get_dest(curr.val, [start.val, start.next.val, end.val])
  end.next = dest.next
  dest.next = start
  curr = curr.next
  #print_ll()
#print_ll()
get_star()
