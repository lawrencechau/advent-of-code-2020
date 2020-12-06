import math

def part_1():
  file = open('input', 'r')
  lines = file.readlines()
  rows = len(lines)
  cols = len(lines[0])

  trees = 0
  col = 0

  for row in range(rows):
    if lines[row][col] == '#':
      trees += 1
    col = (col + 3) % (cols-1)

  return trees

def part_2(slope):
  right, down = slope
  file = open('input', 'r')
  lines = file.readlines()
  rows = len(lines)
  cols = len(lines[0])

  trees = 0
  col = 0

  for row in range(0, rows, down):
    if lines[row][col] == '#':
      trees += 1
    col = (col + right) % (cols-1)

  return trees

print('Part 1')
print(part_1())
print('Part 2')
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
results = list(map(part_2, slopes))
print(math.prod(results))
