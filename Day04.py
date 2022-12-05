with open('Day04data.in') as data:
  pairs = [i for i in data.read().strip().split('\n')]

fully_overlap_count = 0
partial_overlap_count = len(pairs)

for pair in pairs:
  p1, p2 = pair.split(',')
  p1_start, p1_end = map(int, p1.split('-'))
  p2_start, p2_end = map(int, p2.split('-'))
  print(p2_start, p2_end, p1_start, p1_end)

  if (p1_start <= p2_start and p1_end >= p2_end) or (p1_start >= p2_start and p1_end <= p2_end):
    fully_overlap_count +=1
  
  if (p2_start > p1_end) or (p1_start > p2_end):
    partial_overlap_count -=1
  
    
print("Part 1: ", fully_overlap_count)
print("Part 2: ", partial_overlap_count)