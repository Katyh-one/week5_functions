# importing a module - python file
# directly executing a script
# python script can import other modules - goes to the module and runs the code in it
import greetings_functions

print("This is the 'using' file")
# greetings_functions module has a function called say_hello
greetings_functions.say_hello()
greetings_functions.greet_someone('katy')
greetings_functions.greet_someone()

print(f"The name of the use_greetings_functions file is {__name__}")
print(f"The name of the greetings_functions file is {greetings_functions.__name__}")
print("The end")





