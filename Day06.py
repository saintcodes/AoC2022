with open('Day06data.in') as data:
  string = data.readline()

def exec_four_packet(string):
  length = 4

  last_four = string[0:4]
  while len(set(last_four)) < 4:
    length += 1
    last_four = string[length-4:length]
  return length

def exec_fourteen_packet(string):
  length = 14

  last_fourteen = string[0:14]
  while len(set(last_fourteen)) < 14:
    length += 1
    last_fourteen = string[length-14:length]
  return length


print(exec_four_packet(string))
print(exec_fourteen_packet(string))