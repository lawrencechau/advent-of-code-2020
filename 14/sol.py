#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))
#dat = open('input').read().strip().split('\n')
dat = open('example_2').read().strip().split('\n')
m = len(dat)
#n = len(dat[0])

def apply(mask, num):
  num_b = "{0:b}".format(num).zfill(36)
  stack = []
  for i in range(35, -1, -1):
    #print(i, len(mask), len(num_b))
    a, b = mask[i], num_b[i]
    if a == 'X':
      stack.append(b)
    else:
      stack.append(a)
  return int(''.join(stack[::-1]), 2)

def apply_addr(mask, addr):
  addr_b = "{0:b}".format(addr).zfill(36)
  stack = [[]]
  for i in range(35, -1, -1):
    a, b = mask[i], addr_b[i]
    #print(a, b, i)
    #print(stack)
    if a == '1':
      for l in stack:
        l.append('1')
    elif a == '0':
      for l in stack:
        l.append(b)
    else:
      stack.extend(stack)
      for i in range(len(stack)):
        if i < len(stack)//2:
          stack[i].append('0')
        else:
          stack[i].append('1')
  return [int(''.join(s[::-1]) for s in stack]


mask = ''
d = {}
for line in dat:
  #print(line)
  if line.startswith('mask'):
    mask = line.split()[2]
  else:
    space, _, val = line.split()
    addr = space[4:-1]
    #d[addr] = apply(mask, int(val))
    for a in apply_addr(mask, int(addr)):
      print(a)
      d[a] = int(val)

print(sum(d.values()))

    

