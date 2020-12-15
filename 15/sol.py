#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))
#dat = open('input').read().strip().split('\n')
#dat = open('example').read().strip().split(',')
dat = open('input').read().strip().split(',')
m = len(dat)
#n = len(dat[0])
hi = 30000001
#hi = 2021

d = {int(num):idx+1 for idx, num in enumerate(dat[:-1])}
turn = m
prev = int(dat[-1])

for i in range(m+1, hi):
  if prev not in d:
    d[prev] = i-1
    prev = 0
  else:
    temp = prev
    prev = i-1-d[prev]
    d[temp] = i-1 
print(prev)
