# Brute Force
# 5641
# 00:19:50

dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example').read().strip().split('\n')))
#print(type(dat))
n = len(dat)

dat = set(dat)
target = max(dat)+3
perm = 0
ans = []
pos = set()
lo, hi = 0, 0

def backtrack(prev=0):
  global lo, hi
  global perm
  if not dat or target == prev + 3:
    #print(lo, hi+1)
    print(ans)
    pos.add(frozenset(ans))
    return

  for num in range(prev+4):
    if num in dat:
      dat.remove(num)
      diff = abs(num-prev)
      if diff == 1:
        lo += 1
      elif diff == 3:
        hi += 1
      ans.append(num)
      backtrack(num)
      ans.pop()
      dat.add(num)
      if diff == 1:
        lo -= 1
      elif diff == 3:
        hi -= 1

# Maybe do some caching on the num you've seen and use that to determine whether a possible set
backtrack()
print(len(pos))
