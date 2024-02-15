
# create a function
# define a function
# take in parameters in the brackets - can be empty
def say_hello():
    print('hello world!')
    print('goodbye world')
    print("~" * 50)

# functions use verbs - doing words

# default value unless otherwise passed
def greet_someone(name="World"):
    print(f"Welcome {name}!")
    print(f"Hi {name.capitalize()}, how are you today?")
    print("~" * 50)

# top line of function is a signature


def display_info(name, lucky_number, *, hobby='Coding', favourite_place='Pycharm'):
    print("*" * 50)
    print(f"Your name is: {name}.\nYour lucky number is: {lucky_number}.\nYour hobby is {hobby}.\nYour fav place is {favourite_place} ")
    print("*" * 50)

def display_inf2(name, lucky_number, hobby='Coding', favourite_place='Pycharm'):
    print("*" * 50)
    print(f"Your name is: {name}.\nYour lucky number is: {lucky_number}.\nYour hobby is {hobby}.\nYour fav place is {favourite_place} ")
    print("*" * 50)

#  the 'main' trick
# when function dev runs this file they should see the tests
# when the using dev imports this module they shouldn't see the tests
# scenario - developer function created, user to call the function
# shouldn't need to know how the functions work
# test it but not have it run when the module is called
#  __ built in double underscore dunderscore
# when run script yourself you are the first file that is run
# entry point - first file that will be executed
# name attribute , main string
# so any script that you run will be main
if __name__ == "__main__":
    #  test the function
    print("This is a test")
    say_hello()
    greet_someone('rana')
    print("This is the 'functions' file")
    print(f"The name of the greetings_function file is {__name__}")
    # due to the * in between lucky number and hobby - forces parameters to be named
    # why use this?
    display_info('Katy', 10, hobby='eating', favourite_place='home')
    # overwrite the default if you want to
    display_info('Katy', 10, favourite_place='Leeds')
    print("The end of the tests")




