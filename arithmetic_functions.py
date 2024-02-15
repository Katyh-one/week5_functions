
# add function
def add(number1, number2):
    answer = int(number1) + int(number2)
    # hands back the answer to the caller
    return answer


def subtract(number1, number2):
    answer = int(number1) - int(number2)
    # hands back the answer to the caller
    return answer


# variadic functions takes multiple parameters
def add_many(*numbers):
    answer = 0
    for number in numbers:
        answer += int(number)
    return answer

# return - can only return one object - boolean, string etc tuple, list, dictionary multiple items in it
def do_magic(number1, number2):
    number1_squared = number1 * number1
    number2_doubled = number2 * 2
    # returned as tuple as separated by comma
    return number1_squared, number2_doubled

if __name__ == "__main__":
    result = subtract(100, 20)
    print(f"i have subtracted and the results is {result}")


