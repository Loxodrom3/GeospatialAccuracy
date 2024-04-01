# Write your code here :-)
# initialize list
test_list = [5, -6, 7, -8, -10]

# printing original list
print("The original list is : " + str(test_list))

# Absolute value of list elements
# using abs() + list comprehension
res = [abs(ele) for ele in test_list]

# printing result
print("Absolute value list  : " + str(res))
