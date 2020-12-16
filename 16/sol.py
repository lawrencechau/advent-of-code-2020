from collections import defaultdict
# int
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))

 
#dat = open('example').read().strip().split('\n')
dat = open('e_2').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')

m = len(dat)
#n = len(dat[0])

seen = set()
mine = None
nearby = []

i = 0

fields = defaultdict(list)
# Parse fields
while dat[i]:
  idx = dat[i].index(':')
  ranges = dat[i][idx+2:].split(' or ')
  f = dat[i][:idx]
  for r in ranges:
    lo, hi = r.split('-')
    lo, hi = int(lo), int(hi)
    for val in range(lo, hi+1):
      seen.add(val)
    fields[f].append((lo,hi))
  i += 1

print(fields)
i+=2
# Parse my tickets
while dat[i]:
  mine = [int(num_s) for num_s in dat[i].split(',')]
  i += 1

i += 2
not_valid = []
valid = []
while i < m and dat[i]:
  l = list(map(int, dat[i].split(',')))
  for num in l:
    if num not in seen:
      #not_valid.append(num)
      continue
  valid.append(l)
  i += 1

print(sum(not_valid))

field_idx = {}
occ = seen()
def check(idx=0):
  if idx == len(valid):
    res = 1
    for k, v in field_idx.items():
      if k.startswith('departure'):
        res *= mine[v]
    print(f"FINAL: {res}")
    return True
  l = list(map(int, dat[i].split(',')))
    
  
  return False

def build(sample):
  s = list(map(int, sample.split(',')))
  for f, ranges in fields.items():
    for r in ranges:
      
