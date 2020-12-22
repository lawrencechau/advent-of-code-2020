import math
from collections import defaultdict, deque

#dat = open('example').read().strip().split('\n\n')
#dat = open('example').read().strip().split('\n\n')
dat = open('input').read().strip().split('\n\n')

def build_deck(block):
  return deque([int(n) for n in block.split('\n')[1:]])
bp1 = build_deck(dat[0])
bp2 = build_deck(dat[1])
m = len(dat)


def calc_winner(winner):
  print('Winner')
  print(sum([n*(idx+1) for idx, n in enumerate(list(winner)[::-1])]))
  exit()

def play_game(p1, p2, r=0):
  seen = {}
  i = 0
  while p1 and p2:
    i += 1
    #print(f'Round {r} (Game {i})')
    p1f, p2f = tuple(p1), tuple(p2)
    #print(seen)
    if p1f in seen and seen[p1f] == p2f:
      print('Ended by repeat')
      calc_winner(p1)
      return True
    else:
      seen[p1f] = p2f

    p1c, p2c = p1.popleft(), p2.popleft()

    if len(p1) >= p1c and len(p2) >= p2c:
      np1, np2 = deque(list(p1)[:p1c].copy()), deque(list(p2)[:p2c].copy())
      #print(f'{r} - Playing subgame')
      #print(p1c,p1, p2c,p2)
      if play_game(np1, np2, r+1):
        p1.append(p1c)
        p1.append(p2c)
      else:
        p2.append(p2c)
        p2.append(p1c)
      #print(f'{r} - End subgame')
      #print(p1, p2)
    elif p1c > p2c:
      p1.append(p1c)
      p1.append(p2c)
    else:
      p2.append(p2c)
      p2.append(p1c)

  return True if p1 else False 

winner = play_game(bp1, bp2)
calc_winner(bp1 if winner else bp2)
