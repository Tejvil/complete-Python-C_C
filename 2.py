# is operator
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because a and b refer to the same list object
print(a is c)  # False, because a and c refer to different list objects with the same values

# in operatror
my_list = [1, 2, 3, 4, 5]

# Check if a value exists in the list
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

# ternary operator
x = 5
y = 10

result = x if x > y else y
print(result)  # Output will be 10 because x is not greater than y


