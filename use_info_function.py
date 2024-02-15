from greetings_functions import display_inf2 as display
# from greetings_functions import display_info
# import a specific function not all of them
# name collision when you import things with the same name as what you already have
# as gives it an alias

display('Cherina', 7, favourite_place='bed.')

# used when we call the function
anagha_info = 'Anagha', 9, 'reading', 'mumbai'
display(*anagha_info)


