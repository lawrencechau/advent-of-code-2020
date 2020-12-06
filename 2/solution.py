from collections import Counter

def part_1():
  file = open('input', 'r')
  lines = file.readlines()

  valids = 0

  for line in lines:
    split_line = line.split()
    minimum, maximum = split_line[0].split('-')
    minimum, maximum = int(minimum), int(maximum)
    target_char = split_line[1][:-1]
    password = split_line[2]

    target_char_count = Counter(password).get(target_char, 0)
    valids += 1 if minimum <= target_char_count <= maximum else 0

  return valids

def part_2():
  file = open('input', 'r')
  lines = file.readlines()

  valids = 0

  for line in lines:
    split_line = line.split()
    minimum, maximum = split_line[0].split('-')
    lo, hi = int(minimum)-1, int(maximum)-1
    target_char = split_line[1][:-1]
    password = split_line[2]

    lo_has = password[lo] == target_char
    hi_has = password[hi] == target_char

    valids += 1 if lo_has ^ hi_has else 0

  return valids

print('Part 1')
print(part_1())
print('Part 2')
print(part_2())
