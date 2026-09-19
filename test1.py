# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.difference(st1)) # set() : st2 - st1
# print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2  : st2 - st1
# print(st2 - st1)
# print(st1 - st2)

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#     if count == 3:
#         count += 1
#         continue

# numbers = [0, 1, 2, 3, 4, 5]
# for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
#     print(number)       # the numbers will be printed line by line, from 0 to 5

# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }

# for a, b in person.items():
#     print(a, b) # this way we get both keys and values printed out

# a=1
# b=6
# c=9
# x=(-b+(b**2-4*a*c)**0.5)/2*a
# print(x)

# import statistics

# data = [1, 2, 2, 3, 4, 4]

# # Returns a single mode (the first one found if there's a tie)
# single_mode = statistics.mode(data)
# print(f"Single Mode: {single_mode}")  # Output: 2

# # Returns a list of all modes if there is a tie
# all_modes = statistics.multimode(data)
# print(f"All Modes: {all_modes}")      # Output: [2, 4]

import random
import string

# def generate_user_id(length=6):
#     # Combines uppercase letters, lowercase letters, and digits 0-9
#     characters = string.ascii_letters + string.digits
    
#     print(characters)
#     # Chooses 6 random characters and joins them into a single string
#     return ''.join(random.choice(characters) for _ in range(length))

# # Example usage:
# print(generate_user_id())  # Outputs something like: "k7Xp2W"

# def random_user_id(length=6):
#     a = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#     return ''.join(random.choice(a) for _ in range(length))

# print(random_user_id())

# Assuming your input list is:
countries_input = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Python dictionary for quick ISO 3-letter code lookups
iso_codes = {
    'FINLAND': 'FIN',
    'SWEDEN': 'SWE',
    'NORWAY': 'NOR'
}

output = [
    [country.upper(), iso_codes[country.upper()], capital.upper()] 
    for sublist in countries_input 
    for country, capital in sublist
]

print(output)
