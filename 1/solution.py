def solution1():
  file = open('input', 'r')
  lines = file.readlines()

  seen= set()
  for line in lines:
    num = int(line)
    if 2020 - num in seen:
      print(num * (2020-num))
      return 
    seen.add(num)

  print('No match found')

def solution2():
  file = open('input', 'r')
  lines = file.readlines()
  nums = sorted(int(num) for num in lines)

  for i in range(len(nums)):
    find_match(i, nums)

def find_match(idx, nums):
  lo, hi = idx+1, len(nums)-1
  if lo < hi:
    target = 2020 - nums[idx]
    while lo < hi:
      pair = nums[lo] + nums[hi]
      if pair < target:
        lo += 1
      elif pair > target:
        hi -= 1
      else:
        print(f"{nums[idx]} + {nums[lo]} + {nums[hi]} = {nums[idx] + nums[lo] + nums[hi]}")
        print(f"{nums[idx]} * {nums[lo]} * {nums[hi]} = {nums[idx] * nums[lo] * nums[hi]}")
        exit()

print('Part 1')
solution1()
print('Part 2')
solution2()
