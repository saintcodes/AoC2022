with open('Day03data.in') as data:
  rucksack = [i for i in data.read().strip().split('\n')]

print(rucksack[0], rucksack[1])