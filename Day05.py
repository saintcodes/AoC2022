with open('Day05data.in') as data:
  stacks = [i for i in data.read().split('\n')]

# print(stacks[8])
transformed_dict = {}

for char in stacks[8]:
  if char != " ":
    transformed_dict[int(char)] = []

for stack in reversed(stacks[0:8]):
  key = 1
  pos = 1
  print(transformed_dict[key])
  while (key < 10):
    if (stack[pos] != "[") and (stack[pos] != "]") and (stack[pos] != " "):
      transformed_dict[key] += [stack[pos]]
    key +=1
    pos +=4


print(transformed_dict)


#             [G] [W]         [Q]    
# [Z]         [Q] [M]     [J] [F]    
# [V]         [V] [S] [F] [N] [R]    
# [T]         [F] [C] [H] [F] [W] [P]
# [B] [L]     [L] [J] [C] [V] [D] [V]
# [J] [V] [F] [N] [T] [T] [C] [Z] [W]
# [G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
# [R] [J] [S] [Z] [R] [S] [D] [L] [J]
#  1   2   3   4   5   6   7   8   9 