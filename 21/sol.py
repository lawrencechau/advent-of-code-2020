"""

dairy: { mxmxvkd kfcds sqjhc nhms }, {fvjkl sbzzf mxmxvkd}
fish: {sqjhc mxmxvkd sbzzf}, {mxmxvkd kfcds sqjhc nhms}
soy: {sqjhc fvjkl}

#mxmxvkd: 3
kfcds: 1
#sqjhc: 3
nhms: 1
trh: 1
#fvjkl: 2
sbzzf: 2

allergen:

mxmxvkd: dairy, fish
sqjhc: fish, soy
fvjkl: soy

"""
import math
from collections import defaultdict
#dat = list(map(int, open('input').read().strip().split('\n')))
#dat = list(map(int, open('ex').read().strip().split('\n')))

#dat = open('example').read().strip().split('\n')
dat = open('input').read().strip().split('\n')

m = len(dat)

count = defaultdict(int)
allergens = defaultdict(set)
ingredients = defaultdict(set)

for l in dat:
  ings, allers = l.split(' (contains ', 1)
  ings = ings.split()
  allers = allers[:-1].split(', ')
  for aller in allers:
    allergens[aller].add(frozenset(ings))
  for ing in ings:
    count[ing] += 1

for aller, cands in allergens.items():
  for cand in frozenset.intersection(*list(cands)):
    ingredients[cand].add(aller)

#print(allergens)
#print(count)
#print(ingredients)

print(sum(v for k, v in count.items() if k not in ingredients))

final = {}
while ingredients:
  curr = {}
  for ing, allers in ingredients.items():
    if len(allers) == 1:
      curr[list(allers)[0]] = ing
  #print(curr)
  for ning in curr.keys():
    for ing in list(ingredients.keys()):
      if ning in ingredients[ing]:
        print(ing, ning)
        ingredients[ing].remove(ning)
      if not ingredients[ing]:
        del ingredients[ing]
  print(ingredients)
  final.update(curr)
print(final)
print(','.join([ing for _, ing in sorted((k,v) for k,v in final.items())]))
