import collections

lines = open('example').read().strip().split('\n')

def domask(arg, mask):
  print('===')
  print(f"Mask: {mask}")
  print(f"Arg: {arg}")
  # Sets the 1s
  arg |= int(mask.replace('X', '0'), 2)
  print(f"Arg: {arg}")
  # Clears anywhere that should be 0s
  arg &= int(mask.replace('X', '1'), 2)
  print(f"Arg: {arg}")
  print('===')
  return arg

def allmask(pos, mask):
  if not mask:
    yield 0
  else:
    if mask[-1] == '0':
      for m in allmasks(pos // 2, mask[:-1]):
        yield (2*m) + (pos%2)
    if mask[-1] == '1':
      for m in allmasks(pos // 2, mask[:-1]):
        yield (2*m) + 1
    if mask[-1] == 'X':
      for m in allmasks(pos // 2, mask[:-1]):
        yield 2*m + 0
        yield 2*m + 1

mask = None
mem = collections.defaultdict(int)
for line in lines:
  op, arg = line.split(' = ')
  if op == 'mask':
    mask = arg
  else:
    pos = int(op[4:-1])
    # mem[pos] = domask(int(arg), mask)
    for m in allmask(pos, mask):
      mem[m] = int(arg)

print(sum(mem.values()))
