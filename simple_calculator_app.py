import arithmetic_functions

# help(arithmetic_functions)

result = None
value1 = 123
value2 = 500
# passing the arguments positional - first, second
result = arithmetic_functions.add(value1, value2)
print(f"the first result is: {result}")

result = arithmetic_functions.add(value1, 42)
print(f"the second result is: {result}")

result = arithmetic_functions.subtract(value2, value1)
print(f"i have subtracted and the results is {result}")
# no return
# print doesn't return anything
# input does return something - has return statement in it
# enumerate returns a tuple
# firstname = input("What is your name?")
# print(f"Your firstname is: {firstname}")

# not used due to more typing and less efficient
# can pass in different order
subtract_result2 = arithmetic_functions.subtract(number1=2,number2=10)
print(subtract_result2)

# calling the variadic function
add_a = arithmetic_functions.add_many(2, 5, 7, 90, 100, 125)
print(f"variadic function {add_a}")
# or as a tuple
nums = 20, 25, 30, 50, 60
# call the function and unpack the tuple
add_b = arithmetic_functions.add_many(*nums)
print(f"variadic function b {add_b}")

squared, doubled = arithmetic_functions.do_magic(value1, value2)
print(squared, doubled)
