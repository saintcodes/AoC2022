# msg = "hello hmm"
# print(msg)

#getting our data from Day02data.input file
with open('Day02data.in') as data:
  games = [i for i in data.read().strip().split('\n')]


# possible outcomes of p1
# LEFT RIGHT | OUTCOME | RIGHT + OUTCOME = TOTAL
# -------------------------------
# A X = DRAW = 1 + 3 = 4
# A Y = WIN = 2 + 6 = 8
# A Z = LOSS = 3 + 0 = 3
# B X = LOSS = 1 + 0 = 1
# B Y = DRAW = 2 + 3 = 5
# B Z = WIN = 3 + 6 = 9
# C X = WIN = 1 + 6 = 7
# C Y = LOSS = 2 + 0 = 2
# C Z = DRAW = 3 + 3 = 6
p1_outcomes = {
  "A X": 4, "A Y": 8, "A Z": 3,
  "B X": 1, "B Y": 5, "B Z": 9,
  "C X": 7, "C Y": 2, "C Z": 6
}

total_points_p1 = 0
for game in games:
  total_points_p1 += p1_outcomes[game]

# possible outcomes of p2
# LEFT RIGHT | OUTCOME | RIGHT + OUTCOME = TOTAL
# -------------------------------
# A X = LOSS = 3 + 0 = 3
# A Y = DRAW = 1 + 3 = 4
# A Z = WIN = 2 + 6 = 8
# B X = LOSS = 1 + 0 = 1
# B Y = DRAW = 2 + 3 = 5
# B Z = WIN = 3 + 6 = 9
# C X = LOSS = 2 + 0 = 2
# C Y = DRAW = 3 + 3 = 6
# C Z = WIN = 1 + 6 = 7

p2_outcomes = {
  "A X": 3, "A Y": 4, "A Z": 8,
  "B X": 1, "B Y": 5, "B Z": 9,
  "C X": 2, "C Y": 6, "C Z": 7
}

total_points_p2 = 0
for game in games:
  total_points_p2 += p2_outcomes[game]

print('p1 ', total_points_p1)
print('p2 ', total_points_p2)






