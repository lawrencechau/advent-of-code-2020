#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))
dat = open('input').read().strip().split('\n')
#dat = open('example').read().strip().split('\n')
m = len(dat)
#n = len(dat[0])

start = int(dat[0])
# ids = [int(bus) for bus in dat[1].split(',') if bus != 'x']
loc = [int(bus) for bus in dat[1].split(',') if bus != 'x']
ids = {int(bus):(idx, 0)  for idx, bus in enumerate(dat[1].split(',')) if bus != 'x'}
seen = {bus: set() for bus in ids.keys()}

# part 1
# res = float('inf')
# res_id = 0
# 
# for bus in ids:
#   curr = 0
#   while curr <= start:
#     curr += bus
#   if curr-start < res:
#     res = curr-start
#     res_id = bus
# 
# print(res*res_id)

# some dumb attempt at part 2
def recursive(prev_idx, idx, time):
  prev_bus = loc[prev_idx]
  bus = loc[idx] 
  start = ids[bus][1]
  offset = ids[bus][0]-ids[prev_bus][0]
  curr = time
  target = time+1+offset
  while True:
    curr += bus
    seen[bus].add(curr) 
    if curr == target:
      recursive(idx, 
