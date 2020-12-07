def get_bag_and_neighbor(line):
  bag = line[:line.find('bags')-1]
  neighbor_string = line[line.find('contain ') + len('contain '):-1]
  neighbors = set()
  if 'no other bags' in neighbor_string:
    return bag, neighbors

  for neighbor_bag_string in neighbor_string.split(', '):
    bag_split = neighbor_bag_string.split(' ')
    neighbors.add((int(bag_split[0]), ' '.join(bag_split[1:-1])))
  
  return bag, neighbors


bags = {}
file = open('input', 'r')
lines = file.readlines()

for line in lines:
  parent, neighbor = get_bag_and_neighbor(line)
  bags[parent] = neighbor


def bag_contains_target(bag, target):
  if not bag:
    return False
  elif target in [color for count, color in bag]:
    return True
  return any(bag_contains_target(bags[n], target) for n in [color for count, color in bag])

def part_1():
  return sum(bag_contains_target(n, 'shiny gold') for n in bags.values())

def part_2(color):
  res = 0
  for count, neighbor in bags[color]:
    res += count + count * part_2(neighbor)
  return res
    
  

print('Part 1')
print(part_1())
print('-------')
print('Part 2')
print(part_2('shiny gold'))
