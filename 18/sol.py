import math
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('ex').read().strip().split('\n')))

dat = open('ex').read().strip().split('\n')
#dat = open('input').read().strip().split('\n')

m = len(dat)
#n = len(dat[0])

res = 0
stack = []
op_stack = []
#prev = 0
prev = 1
op = '*'

for l in dat:
  for i, c  in enumerate(l):
    if c.isdigit():
      curr = int(c)
      if op == '+':
        #prev += curr
        prev += curr
      else:
        stack.append(prev)
        prev = curr
    elif c == '(':
      stack.append(prev)
      op_stack.append(op)
      #prev = 0
      prev = 1
      op = '*'
    elif c == ')':
      if op_stack[-1] == '+':
        stack[-1] += prev
      op_stack.pop()
      prev = stack[-1]
      stack.pop()
    elif c in ('+', '*'):
      op = c
    if i == len(l)-1:
      stack.append(prev)
    print(c, prev)
  print(stack)
  #print(prev)
  res += math.prod(stack)
  stack = []
  op_stack = []
  prev = 1
  op = '+'

print(res)
    
