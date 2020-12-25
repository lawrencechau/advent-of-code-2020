import math
from collections import defaultdict, deque

#card_pk, door_pk = list(map(int, open('example').read().strip().split('\n')))
card_pk, door_pk = list(map(int, open('input').read().strip().split('\n')))

subj_num = 7

def transform(val, num):
  val *= num
  val %= 20201227
  return val

def get_ls(pk):
  ls = 0
  val = 1
  while val != pk:
    val = transform(val, subj_num)
    ls += 1
  return ls

def get_encryption_key(pk, ls):
  val = 1
  for _ in range(ls):
    val = transform(val, pk)
  return val

card_ls = get_ls(card_pk)
door_ls = get_ls(door_pk)
print(card_ls, door_ls)

card_ek  = get_encryption_key(door_pk, card_ls)
door_ek  = get_encryption_key(card_pk, door_ls)
print(card_ek, door_ek)
