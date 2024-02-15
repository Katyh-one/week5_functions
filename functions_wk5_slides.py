# slide 295
# values required by the function are specified within the brackets
# call or invoke function
# reusable block of code - series of instructions
# name and location - that can be invoked using name
# homework - function required - start without function (rock paper scissors)
# write comments before writing the code
# everyone's a player and then compare outcomes to see who wins
# play again?
# tally of total scores
# record scores in a file
# take turns
# positional passing of parameters

# define function using def followed by parameter list
def make_list(val, times):
    res = str(val) * times
    return res
# when you call the function you pass the parameters by assigning them in the brackets
print(make_list('we love chips ', 25))

# slide 296
def change_list(inlist, val, times):
    inlist += str(val) * times
mylist = []
change_list(mylist, 'h', 8)
print(mylist)

# slide 297
# assigning the value when you define the function rather than assigning the value when you call it
# Parameters may only assign default on the right so the parameters you dont want to default should be first
def print_vat(gross, vatpc=17.5, message='Summary: '):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    # print(f"{message} Net: {net:5.2f} Vat: {vat:5.2f}")
    # f stands for floating point - values 0 = position first variable passed, 5 = width, . = precision type
    print(message, 'Net: {0:5.2f} Vat:{1:5.2f}'.format(net,vat))
print_vat(9.55)
print_vat(9.55, message='Final sum: ')

# slide 298
def my_func(file, dir, user='root'):
    print('file: {:}, dir: {:}, to: {:}'.format(file,dir,user))
    # print(f"file: {file} dir: {dir}, to: {user}")
# call the function by position - which value you want in each position
my_func('one','two', 'three')
# as there is already a default value for the third parameter, call the function using values for the first two
my_func('one', 'two')
# call the function by specifying the value for each parameter in the function
my_func(file='one', user='three', dir='two')

# slide 299
# to force someone to specify function parameters by nmame use *
def print_vat(*, gross= 0, vatpc= 17.5, message= 'Summary: '):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} VAT: {1:5.2f}'.format(net, vat))
print_vat(vatpc= 15, gross= 9.55)
print_vat()
# doesnt work as parameters not specified by name
# print_vat(15, 9.55)

# slide 300
# unpacking and variadic functions
def my_func(a, b, c):
    print(a, b, c)
# unpacking by taking a sequence like a tuple and passing it into the function using the *
# the container ie what is in the tuple must contain the right number of elements
mytuple = 23, 45, 67
my_func(*mytuple)

# variadic functions
# takes a variable number of parameters
# * tuple
def my_function(dir, *files):
    print('dir: ', dir, 'files: ', files)
my_function('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt')

# ** indicates dictionary
def print_vat(**kwargs):
    print(kwargs)
print_vat(vatpc=15, gross=9.55, message= 'Summary:')
# to unpack the arguments from the dictionary
# if we didn't use the ** it wouldnt work as it wouldnt recognise the right number of arguments being passed
argsdict = dict(vatpc=15, gross=9.55, message='Summary')
print_vat(**argsdict)

# 302 - returning objects from a function
def calc_vat(gross, vatpc=17.5):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    # stops the execution of the function
    # passes the object back to the caller
    # if you dont use return it will give a reference of None
    return [f'{net:05.2f}, {vat:05.2f}']
result = calc_vat(42.30)
print(calc_vat(9.55))

# # 303 Variables in functions - DO NOT USE
# result = 3
# def scope_test1():
#      # variables assigned within the function body are lost on exit of the function
#      result = 42
# scope_test1()
# print(result)
#
# def scope_test2():
#     # used before the variable to declare as global but are frowned upon
#     global result
#     result = 42
# scope_test2()
# print(result)

# 304 Lambda functions
# short-hand functions
# anonymous - small bit of logic
# very simple - lambda goes in replace of the name - not reused
# ideal for reusing a function within a function
# no return statements allowed
# last thing it returns is what it holds
# a and b are the arguments
# -1 shorter +1 taller - comparing each item to each other item to see where it sits
# conditional expression yes or no - if or else
compare= lambda a,b: -1 if a < b else (+1 if a > b else 0)

x = 42
y= 3
# when passing the function compare we are giving it the arguments x and y
# as x is greater than y it prints 1
print("a>b", compare(x,y))
# adds 1 to each item in the list
# map - (func - is function which map passes each element of the iterable, iter is the iterable to be mapped)
# it's a function that returns the map object of the results after applying the function to each item in list/ tuple etc
source_list = [1,2,3,4,5]
new_list = list(map(lambda a: a+1, source_list))
print(new_list)
# filters - filter(function, sequence)
# function tests if each element of the sequence is true or not
# sequence which needs to be filtered - list sets tuples
# function that filters vowels - looks at the variable and if the letters in the variable are in letters it returns true
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False
# sequence - this is a variable which is then passed into the filter function along with the function above
# and variable sequence
# sequence letters that are also in the variable letters in the above function - letter EE
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# using filter function applies the fun function across each element in the sequence list
filtered = filter(fun, sequence)
print('The filtered letters are:')
# iterates over the returned values in filtered and prints them?
for s in filtered:
	print(s)

