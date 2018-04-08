my_nums = [2, 3, 4, 35, 12, 2, 76, 1, 55, 85, 61, 5]
# less_than_10 = []
# # to list numbers and display the onces less that 10
# # the num variable will not be defined initially but will assume each value of my_nums
# for num in my_nums:
#     if num < 10:
#         # the append adds the required value to the initialized less_than_10
#         less_than_10.append(num)
#         # print(less_than_10)


# print(less_than_10)

# method 2 same as above method 
# the print statement below: 
# 1. initializes an empty array
# 2. begins to append num in the array
# 3. from the list my_nums
# 4. based on the condition that num less or greater than 10
# print([num for num in my_nums if num > 10]) 

# method 3:filter
# lambda is used as an annonemous function which takes num as aurgument 
# and performs the operations after the column. it returns true or false based
# on the outcome of the performed operation

print(list(filter(lambda num: num < 10, my_nums)))


