numbers_list = [1, 2, 3, 5, 8, 13, 15]
print(f"Original list of numbers: {numbers_list}")
# : breaks the signature of the lambda to the body of the function
numbers_plus1_list = list(map(lambda num: num + 1, numbers_list))
print(f"New list of numbers {numbers_plus1_list}")