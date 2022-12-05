with open('Day04data.in') as data:
  pairs = [i for i in data.read().strip().split('\n')]

count = 0

for pair in pairs:
  p1, p2 = pair.split(',')
  p1_start, p1_end = map(int, p1.split('-'))
  p2_start, p2_end = map(int, p2.split('-'))
  print(p2_start, p2_end, p1_start, p1_end)

  if (p1_start <= p2_start and p1_end >= p2_end) or (p1_start >= p2_start and p1_end <= p2_end):
    count +=1
    
print("Part 1: ", count)

# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.