dog = {

}

dog['Name'] = 'Pancake'
dog['Color'] = 'Orange and White'
dog['Breed'] = 'Corgi'
dog['Legs'] = 4
dog['Age'] = 2

print(dog)

Student = {
    'first_name': 'Nico',
    'last_name': 'Justin Tanryo',
    'gender': 'Male', 
    'age': 18, 
    'marital status': 'Not Married', 
    'skills': ['Python', 'MATH'],
    'country': 'Indonesia', 
    'city': 'Bengkalis',
    'address': 'Jalan Tandun' 
}
print(Student)

print(len(Student))

Skills_Value = Student.get('skills')
print(f'{Skills_Value} , {type(Skills_Value)}')

Student['skills'].append('HTML')
Student['skills'].extend(['JavaScrip','C++'])
print(Student)

print(Student.keys())

print(Student.values())

print(Student.items())

del Student['gender']

print(Student)

Student.clear()

print(Student)

del Student