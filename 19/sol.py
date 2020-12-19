from collections import defaultdict
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('ex').read().strip().split('\n')))

#dat = open('example').read().strip().split('\n')
dat = open('example2').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')

m = len(dat)

rules = {}
i = 0
while dat[i]:
  k,v = dat[i].split(': ')
  if k == '8':
    rules[k] = "42 | 42 8"
  elif k == '11':
    rules[k] = "42 31 | 42 11 31"
  else:
    rules[k] = v
  i += 1
print(rules)
#n = len(dat[0])
d = defaultdict(set)

def build(rule):
  print(f"==={rule}===")
  val = rules[rule]
  if rule in d:
    return d[rule]
  if '"' in val:
    d[rule].add(val[1:-1])
  else:
    subrules = val.split(' | ')
    #print(subrules)
    for sr in subrules:
      s = [""]
      for r in sr.split():
        #print(r)
        n = []
        ss = build(r)
        for sss in ss:
          for sc in s:
            n.append(sc+sss)
        s = n
      #print(s)
      for ps in s:
        d[rule].add(ps)
  return d[rule]

build('0')
#print(d)
i += 1
res = 0
while i < m and dat[i]:
  if dat[i] in d['0']:
    res += 1
  i+=1

print(res)
