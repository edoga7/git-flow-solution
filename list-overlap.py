# import random
# list1 = random.sample(range(58) , 20)
# list2 = random.sample(range(40) , 15)
list1 = [2, 2, 3, 4, 4, 5, 8, 8, 9, 20, 38]
list2 = [3, 2, 4, 8, 1, 9, 7]
common_elements = []
for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)
print(list1)
print(list2)
print(common_elements)

# method2:using list set
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
print("------------------method 2 ------------------")
print(list1)
print(list2)
print(list(set(common_elements)))

# method3: using while loop
common_elements = []
# lenght and counter as comparable variables
# in this case counter starts from 0, we keep comparing it to lenght
# until the condition (counter < lenght)is no longer true
# at this point the loop terminates

# the increament statement (counter += 1) increases counter by 1 in each loop, 
# thereby bringing closer to termination 
lenght = len(list1)
counter = 0
while counter < lenght:
    element = list1[counter]
    if element in list2 and element not in common_elements:
        common_elements.append(element)
    counter += 1
print("------------------method 3 ------------------")
print(list1)
print(list2)
print(common_elements)