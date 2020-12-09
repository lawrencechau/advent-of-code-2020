dat = list(map(int, open('input').read().strip().split('\n')))
preamble = 25
#dat = list(map(int, open('example').read().strip().split('\n')))
#preamble = 5
#print(type(dat))
#print(len(dat))
n = len(dat)

def search(target, lo, hi):
  for j in range(lo, hi-1):
    for k in range(j+1, hi):
      if dat[j] + dat[k] == target:
        return True
  return False

target = 0
for i in range(preamble, n):
  lo, hi = i - preamble, i 
  if search(dat[i], lo, hi):
    continue
  else:
    target = dat[i]
    break

lo, hi = 0, 2
run = dat[0] + dat[1]
while target != run:
  run += dat[hi]
  while run > target:
    run -= dat[lo]
    lo += 1
  hi += 1

print(min(dat[lo:hi]) + max(dat[lo:hi]))
