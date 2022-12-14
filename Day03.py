with open('Day03data.in') as data:
  rucksacks = [i for i in data.read().strip().split('\n')]

alphaValues = {
  "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
  "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
  "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
  "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
  "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
  "z": 26,
  "A": 27, "B": 28, "C": 29, "D": 30, "E": 31,
  "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
  "K": 37, "L": 38, "M": 39, "N": 40, "O": 41,
  "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
  "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51,
  "Z": 52
} 

prioritySum = 0

for rucksack in rucksacks:
  firstHalf = set(rucksack[:len(rucksack)//2])
  secondHalf = set(rucksack[len(rucksack)//2:])
  for char in firstHalf:
    if char in secondHalf:
      prioritySum += alphaValues[char]

badgeSum = 0
element = 0

for i in range(0, len(rucksacks), 3):
  ruck1 = set(rucksacks[element])
  ruck2 = set(rucksacks[element + 1])
  ruck3 = set(rucksacks[element + 2])
  
  for char in ruck1:
    if char in ruck2 and char in ruck3:
      badgeSum += alphaValues[char]
  element +=3



print("answer part1: ", prioritySum)
print("answer part2: ", badgeSum)
      