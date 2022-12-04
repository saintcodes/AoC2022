with open('Day03data.in') as data:
  rucksacks = [i for i in data.read().strip().split('\n')]

ruck1 = rucksacks[0]
firstHalf = ruck1[:len(ruck1)//2]
secondHalf = ruck1[len(ruck1)//2:]
print(firstHalf, secondHalf)

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
  "P": 41, "Q": 42, "R": 43, "S": 44, "T": 45,
  "U": 46, "V": 47, "W": 48, "X": 49, "Y": 50,
  "Z": 51
} 

for i in firstHalf:
  if i in secondHalf:
    print(i)

