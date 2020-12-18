import math
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('ex').read().strip().split('\n')))

#dat = open('ex').read().strip().split('\n')
dat = open('input').read().strip().split('\n')

m = len(dat)
#n = len(dat[0])


def calc(line, idx=0):
  if idx >= len(line):
    return line, 1
  stack = []
  prev = 1
  op = '*'
  i = idx
  while i < len(line): 
    c = line[i]
    if c.isdigit():
      curr = int(c)
      if op == '+':
        prev += curr
      else:
        stack.append(prev)
        prev = curr
    elif c == '(':
      i, curr = calc(line, i+1)
      if op == '+':
        prev += curr
      else:
        stack.append(prev)
        prev = curr
    elif c == ')':
      stack.append(prev)
      break
    elif c in ('+', '*'):
      op = c
    if i == len(line)-1:
      stack.append(prev)
      break
    i+=1
  return i, math.prod(stack)

res = 0
# stack = []
# op_stack = []
# #prev = 0
# prev = 1
# op = '*'
for l in dat:
#  for i, c  in enumerate(l):
#    if c.isdigit():
#      curr = int(c)
#      if op == '+':
#        #prev += curr
#        prev += curr
#      else:
#        stack.append(prev)
#        prev = curr
#    elif c == '(':
#      stack.append(prev)
#      op_stack.append(op)
#      #prev = 0
#      prev = 1
#      op = '*'
#    elif c == ')':
#      if op_stack[-1] == '+':
#        stack[-1] += prev
#      op_stack.pop()
#      prev = stack[-1]
#      stack.pop()
#    elif c in ('+', '*'):
#      op = c
#    if i == len(l)-1:
#      stack.append(prev)
#    print(c, prev)
#  print(stack)
#  #print(prev)
#  res += math.prod(stack)
#  stack = []
#  op_stack = []
#  prev = 1
#  op = '+'
  _, ans = calc(l)
  res += ans

print(res)
    
