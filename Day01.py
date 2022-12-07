# msg = "hello hmm"
# print(msg)

#getting our data from Day01data.input file and splitting them by line break
with open('Day01data.in') as data:
  correctedData = [i for i in data.read().strip().split('\n')]

print(correctedData)

#traversing each string in our dataset
maxCalories = 0
maxTwo = 0
maxThree = 0
calories = 0

for item in correctedData:
  if item == "":
    calories = 0
    #converts the string into an integer
  else:
    num = int(item)
    calories += num

  num_data = []
  for x in correctedData:
    if x != "":
      num_data.append(int(x))
      print(num_data)


# largest_integer = max(numbered_Data)  #  39
# numbered_data.remove(largest_integer)
# print(largest_integer)

# second_largest_integer = max(integers)  # 26
#conditionals to determine sorted values
  # third = first = second = -10000
    
  # for i in range(0, correctedData):
    
  #     # If current element is greater
  #     # than first
  #     if (int(correctedData[i]) > first):
        
  #         third = second
  #         second = first
  #         first = correctedData[i]
        

  #     # If arr[i] is in between first
  #     # and second then update second
  #     elif (correctedData[i] > second):
        
  #         third = second
  #         second = correctedData[i]
        
  #     elif (correctedData[i] > third):
  #         third = correctedData[i]
    
  # print("Three largest elements are", first, second, third)


  # if calories > maxCalories:

  #   maxCalories = calories
  # elif calories > maxTwo:
  #   maxTwo = calories
  # elif calories > maxThree:
  #   maxThree = calories
  


print("Part 1", maxCalories)
print("Part 2", first, second, third)
