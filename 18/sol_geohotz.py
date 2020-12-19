fn = 'input'
dat = open(fn).read().strip().split('\n')

class Num:
  def __init__(self, i):
    self.i = i

  def __add__(self, x):
    return Num(self.i * x.i)

  def __mul__(self, x):
    return Num(self.i + x.i)

def my_eval(x):
  s = ''
  in_num = False
  for c in x:
    if c in '0123456789' and not in_num:
      s += 'Num('
      in_num = True
    if in_num and c not in '0123456789':
      s += ')'
      in_num = False
    s += c

  if in_num:
    s += ')'

  return eval(s).i

acc = 0
for x in dat:
  acc += my_eval(x.replace('*','-').replace('+','*').replace('-','+'))
print(acc)
