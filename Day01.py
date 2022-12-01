# msg = "hello hmm"
# print(msg)

#getting our data from Day01data.input file and splitting them by line break
with open('Day01data.in') as data:
  correctedData = [i for i in data.read().strip().split('\n')]


#traversing each string in our dataset
maxCalories = 0
maxTwo = 0
maxThree = 0
calories = 0

for item in correctedData:
  if item == "":
    calories = 0
  else:
    num = int(item)
    calories += num

  if calories > maxCalories:
    maxCalories = calories
  elif calories > maxTwo:
    maxTwo = calories
  elif calories > maxThree
    maxThree = calories
  


print("Part 1", maxCalories)
print("Part 2", maxCalories, maxTwo, maxThree)
