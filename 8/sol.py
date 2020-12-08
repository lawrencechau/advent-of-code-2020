#dat = open('input').read().strip().split('\n')
dat = open('example').read().strip().split('\n')
#print(type(dat))
#print(len(dat))

def get_next(a):
  act, val = dat[a].split(' ')
  if act == 'jmp':
    return a + int(val)
  else:
    return a + 1

idx = 0
fast = get_next(get_next(0))

while idx != fast:
  print(idx, fast)
  idx = get_next(idx)
  fast = get_next(get_next(fast))

print('Finding point')
fast = 0
while idx != fast:
  print(idx, fast)
  idx = get_next(idx)
  fast = get_next(fast)

print('CHANGING')
print(dat[idx])
if 'nop' in dat[idx]:
  dat[idx] = ' '.join(['jmp', dat[idx].split(' ')[1]])
else:
  dat[idx] = ' '.join(['nop', dat[idx].split(' ')[1]])
print(dat[idx])
print()

acc = 0
idx = 0

while idx < len(dat):
  print(idx+1, dat[idx], acc)
  act, val = dat[idx].split(' ')
  val = int(val)
  if act == 'jmp':
    idx += val
  else:
    if act == 'acc':
      acc += val
    idx += 1

print(acc)
