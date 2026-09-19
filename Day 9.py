#Level 1
# Age = int(input('Enter your Age:'))
# if Age >= 18:
#     print('You are old enough to learn to drive.')
# else :
#     print(f'You need {18-Age} more years to learn to drive.')

# My_Age = 17
# Your_Age = int(input('Enter your Age:'))
# if Your_Age > My_Age:
#     if Your_Age-1 == My_Age:
#         print('You are 1 year older than me.')
#     else:
#         print(f'You are {Your_Age-My_Age} years older than me.')
# elif Your_Age < My_Age:
#     if Your_Age == My_Age-1:
#         print('You are 1 year younger than me.')
#     else:
#         print(f'You are {My_Age-Your_Age} years younger than me.')

# a = int(input('Enter number one:'))
# b = int(input('Enter number two:'))
# if a > b :
#     print(f'{a} is greater than {b}')
# elif a < b :
#     print(f'{a} is lesser than {b}')
# elif a == b :
#     print(f'{a} is equal than {b}')
# else:
#     print('Error')

#Level 2
# score = int(input('Enter student score:'))
# if  100 >= score >= 90 :
#     print('A')
# elif 89 >= score >= 80 :
#     print('B')
# elif 79 >= score >= 70 :
#     print('C')
# elif 69 >= score >= 60 :
#     print('D')
# elif 59 >= score >= 0 :
#     print('F')

# month = input('Enter the month:').title()
# if month in ('September', 'October', 'November') :
#     print("Autumn")
# elif month in ('December','January', 'February') :
#     print("Winter")
# elif month in ('March', 'April', 'May') :
#     print("Spring")
# elif month in ('June', 'July', 'August') :
#     print("Summer")
# else:
#     print('Error')

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Enter a fruit:').lower()
# if fruit in fruits:
#     print('That fruit already exist in the list')
# elif fruit not in fruits:
#     fruits.append(fruit)
#     print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
 }

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills)//2])
    if 'Python' in skills:
        print('There is python in skills')

skills = person['skills']
if len(skills) == 2 and 'JavaScript' and 'React' in skills :
    print('He is a front end developer')
elif len(skills) == 3 and 'Node' and 'Python' and 'MongoDB' in skills:
    print('He is a backend developer')
elif len(skills) == 3 and 'React' and ' Node ' and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')

if 'is_married' in person and 'country' in person :
    is_married = person['is_married']
    country = person['country']
    if is_married is True and 'Finland' in country:
        print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')





