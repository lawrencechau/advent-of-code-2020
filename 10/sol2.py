# Caching solution
# 3516
# 1:04:28

dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('example2').read().strip().split('\n')))
#print(type(dat))

dat.append(0)
dat = sorted(dat) 
dat.append(dat[-1]+3)

n = len(dat)

cache = [0] * len(dat)
cache[-1] = 1

for i in range(n-1, -1, -1):
 for j in range(i+1, min(n, i+4)):
  if dat[j] - dat[i] <= 3:
    cache[i] += cache[j]
print(cache)
print(cache[0])
